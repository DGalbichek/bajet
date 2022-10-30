from django.test import TestCase
from expenses.forms import EMPTY_EXPENSE_NAME_ERROR, NewQuickExpenseForm


class NewQuickExpenseFormTest(TestCase):
    def test_form_name_input_has_placeholder_and_css_classes(self):
        form = NewQuickExpenseForm()
        self.assertIn('placeholder="Enter new expense"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = NewQuickExpenseForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [EMPTY_EXPENSE_NAME_ERROR])
