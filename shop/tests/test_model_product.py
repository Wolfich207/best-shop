from django.core.exceptions import ValidationError
from django.test import TestCase
from shop.models import Category, Product
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal


class TestModelProduct(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Электроника',
            url='hi-tech',
        )
        self.product = Product.objects.create(
            title='Телефон',
            description='Что-то очень интересное про телефон',
            picture=SimpleUploadedFile(
                name='test_img.jpg',
                content=b'',
                content_type='image/jpg',
            ),
            url='phone',
            price=Decimal(19999.99),
            category=self.category,

        )

    def test_fields(self):
        self.assertEqual(self.product.title, 'Телефон')
        self.assertEqual(self.product.description, 'Что-то очень интересное про телефон')
        self.assertEqual(self.product.url, 'phone')
        self.assertEqual(self.product.price, Decimal(19999.99))
        self.assertEqual(self.product.category, self.category)

    def test_fields_meta(self):
        self.assertFalse(self.product._meta.get_field('title').blank)
        self.assertFalse(self.product._meta.get_field('title').null)
        self.assertFalse(self.product._meta.get_field('title').unique)

        self.assertFalse(self.product._meta.get_field('url').blank)
        self.assertFalse(self.product._meta.get_field('url').null)
        self.assertTrue(self.product._meta.get_field('url').unique)

        self.assertTrue(self.product._meta.get_field('description').blank)
        self.assertFalse(self.product._meta.get_field('description').null)

        self.assertFalse(self.product._meta.get_field('price').blank)
        self.assertFalse(self.product._meta.get_field('price').null)

        self.assertFalse(self.product._meta.get_field('category').blank)
        self.assertFalse(self.product._meta.get_field('category').null)

    def test_str(self):
        self.assertEqual(str(self.product), 'Телефон')

    def test_get_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(), '/phone/')

    def test_picture(self):
        self.assertIn('test_img', self.product.picture.name)

    def test_negative_price(self):
        with self.assertRaises(ValidationError):
            self.product.price = -10
            self.product.clean()
