from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from expenses.models import Expense


class ExpenseModelTest(TestCase):
    def test_cannot_save_expense_with_blank_values(self):
        combs = [
            {'name': '', 'amount': 0, 'date': timezone.now()},
            {'name': 'Bla', 'amount': 0, 'date': ''},
        ]
        for c in combs:
            expense = Expense(**c)
            with self.assertRaises(ValidationError):
                expense.save()
                expense.full_clean()
