from django.test import TestCase
from .forms import itemForms


class test_itenform(TestCase):

    def test_item_name_required(self):
        form = itemForms({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name',form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


    def test_done_field_is_not_required(self):
        form = itemForms({'name': 'test to do item'})
        self.assertTrue(form.is_valid())


    def test_fieldds_are_explisit_for_metaclass(self):
        form = itemForms()
        self.assertEqual(form.Meta.fields,['name', 'done'])