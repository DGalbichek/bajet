from django.core.exceptions import ValidationError
from django.test import TestCase
from expenses.models import Expense


class ExpenseModelTest(TestCase):
    def test_cannot_save_expense_with_blank_name(self):
        expense = Expense(name='', amount=0)
        with self.assertRaises(ValidationError):
            expense.save()
            expense.full_clean()
