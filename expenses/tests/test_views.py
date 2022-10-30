from django.test import TestCase
from django.utils.html import escape
from expenses.forms import EMPTY_EXPENSE_NAME_ERROR, NewQuickExpenseForm
from expenses.models import Expense


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_new_quick_expense_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], NewQuickExpenseForm)

    def test_displays_recent_expenses(self):
        expense = Expense.objects.create(name='Grocery shopping', amount=12.34)
        response = self.client.get('/')
        self.assertContains(response, expense.name)

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'name': 'Grocery shopping', 'amount': 12.34})

        self.assertEqual(Expense.objects.count(), 1)
        new_expense = Expense.objects.first()
        self.assertEqual(new_expense.name, 'Grocery shopping')
        self.assertEqual(new_expense.amount, 12.34)

    def test_POST_stays_on_home_page(self):
        response = self.client.post('/', data={'name': 'Grocery shopping', 'amount': 12.34})
        self.assertTemplateUsed(response, 'home.html')

    def _post_invalid_input(self):
        return self.client.post('/', data={'name': ''})

    def test_for_invalid_input_nothing_saved_to_db(self):
        self._post_invalid_input()
        self.assertEqual(Expense.objects.count(), 0)

    def test_for_invalid_input_renders_template(self):
        response = self._post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_for_invalid_input_passes_form_to_template(self):
        response = self._post_invalid_input()
        self.assertIsInstance(response.context['form'], NewQuickExpenseForm)

    def test_for_invalid_input_shows_error_on_page(self):
        response = self._post_invalid_input()
        self.assertContains(response, escape(EMPTY_EXPENSE_NAME_ERROR))
