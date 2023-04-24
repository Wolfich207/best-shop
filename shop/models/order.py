from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from django.db.models import (
    Model,
    CharField,
    TextField,
    DecimalField, Sum,
)


class Order(Model):
    user_name = CharField(
        'Имя Фамилия',
        max_length=200,
    )
    phone = CharField(
        'телефон',
        max_length=200,
    )
    address = TextField(
        'Адрес',
        blank=False,
    )
    delivery_price = DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0, "цена должна быть больше 0")]
    )

    @property
    def amount(self):
        return self.basket_set.aggregate(amount=Sum('amount')).get('amount', None)

    def clean(self):
        if self.price < 0:
            raise ValidationError('цена должна быть больше 0')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        db_table = 'orders'
