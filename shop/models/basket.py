from django.db.models import (
    Model,
    ForeignKey,
    DecimalField,
    SET_NULL,
    CASCADE,
    PositiveIntegerField,
)

from shop.models import Product, Order


class Basket(Model):
    product = ForeignKey(
        Product,
        null=True,
        on_delete=SET_NULL,
        verbose_name='товар',
    )
    order = ForeignKey(
        Order,
        on_delete=CASCADE,
        verbose_name='заказ',
    )
    count = PositiveIntegerField(
        default=1,
        verbose_name='количество товара',
    )
    amount = DecimalField(
        editable=False,
        max_digits=8,
        decimal_places=2,
        null=True,
        verbose_name='цена заказа',
    )

    def save(self, *args, **kwargs):
        self.amount = self.product.price * self.count
        super(Basket, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
        db_table = 'baskets'
