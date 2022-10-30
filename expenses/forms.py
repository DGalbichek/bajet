from django import forms
from expenses.models import Expense

EMPTY_EXPENSE_NAME_ERROR = "You can't add an expense without a name"


class NewQuickExpenseForm(forms.models.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount')
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter new expense',
                'class': 'form-control input-lg'
            }),
        }
        error_messages = {
            'name': {'required': EMPTY_EXPENSE_NAME_ERROR}
        }
