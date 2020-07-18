from django.test import TestCase
from .models import item

class TestModels(TestCase):

    def test_Code_default_to_false(self):
        Item = item.objects.create(name='Test to do')
        self.assertFalse(Item.done)

    def test_item_string_method(self):
        Item = item.objects.create(name='Test to do')
        self.assertEqual(str(Item), 'Test to do')