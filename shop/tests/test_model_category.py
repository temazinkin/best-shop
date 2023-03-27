from django.test import TestCase
from shop.models import Category


class TestModelCategory(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Электроника',
            url='hi-tech',
        )

    def test_fields(self):
        self.assertEqual(self.category.title, 'Электроника')
        self.assertEqual(self.category.url, 'hi-tech')

    def test_fields_meta(self):
        self.assertFalse(self.category._meta.get_field('title').blank)
        self.assertFalse(self.category._meta.get_field('title').null)
        self.assertFalse(self.category._meta.get_field('title').unique)
        self.assertFalse(self.category._meta.get_field('url').blank)
        self.assertFalse(self.category._meta.get_field('url').null)
        self.assertTrue(self.category._meta.get_field('url').unique)

    def test_str(self):
        self.assertEqual(str(self.category), 'Электроника')

    def test_get_absolute_url(self):
        self.assertEqual(self.category.get_absolute_url(), '/all/hi-tech/')
