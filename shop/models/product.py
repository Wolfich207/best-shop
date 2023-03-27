from django.core.validators import MinValueValidator

from django.db.models import (
    Model,
    PROTECT,
    CharField,
    SlugField,
    ImageField,
    DecimalField,
    ForeignKey,
)

from shop.models import Category

from django.urls import reverse


class Product(Model):
    title = CharField(
        'название',
        max_length=200,
    )
    description = CharField(
        'описание',
        max_length=700,
        blank=True,
    )
    picture = ImageField(
        'изображение',
        blank=True,
        null=True,
    )
    url = SlugField(
        'URL',
        unique=True,
    )
    price = DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0, "цена должна быть не меньше 0")]
    )
    category_for_products = ForeignKey(
        Category,
        verbose_name='категория',
        on_delete=PROTECT,
    )

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse(
            'product',
            kwargs={
                'url': self.url,
            }
        )


class Meta:
    verbose_name = 'товар'
    verbose_name_plural = 'товары'
    db_table = 'products'