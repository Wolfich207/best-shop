from django.test import TestCase
from shop.models import Category, Product


class TestModelProduct(TestCase):
    def setUp(self):
        self.product = Product.object.create(
            title='Телефон',
            description='',
            picture='',
            url='phone',
            price='19999,99',
            category=self.category,

        )
        self.category = Category.objects.create(
            title='Электроника',
            url='hi-tech',
        )

    def test_fields(self):
        self.assertEqual(self.category.title, 'Электроника')
        self.assertEqual(self.category.url, 'hi-tech')
