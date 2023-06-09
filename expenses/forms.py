from django import forms
from expenses.models import Expense

EMPTY_EXPENSE_DATE_ERROR = "You can't add an expense without a date"
EMPTY_EXPENSE_NAME_ERROR = "You can't add an expense without a name"


class NewQuickExpenseForm(forms.models.ModelForm):
    class Meta:
        model = Expense
        fields = ('date', 'name', 'amount', 'category', 'paid_by', 'added_by')
        widgets = {
            'date': forms.fields.TextInput(attrs={
                'placeholder': 'yyyy-mm-dd',
                'class': 'form-control input-lg datepicker'
            }),
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter new expense',
                'class': 'form-control input-lg'
            }),
            'amount': forms.fields.TextInput(attrs={
                'class': 'form-control input-lg'
            }),
            'category': forms.fields.Select(attrs={
                'class': 'form-control input-lg'
            }),
            'paid_by': forms.HiddenInput(),
            'added_by': forms.HiddenInput(),
        }
        error_messages = {
            'date': {'required': EMPTY_EXPENSE_DATE_ERROR},
            'name': {'required': EMPTY_EXPENSE_NAME_ERROR}
        }
