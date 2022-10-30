from django.shortcuts import render
from .forms import NewQuickExpenseForm
from .models import Expense


def home_page(request):
    new_quick_expense_form = NewQuickExpenseForm(data=request.POST)
    if new_quick_expense_form.is_valid():
        new_quick_expense_form.save()
        new_quick_expense_form = NewQuickExpenseForm()
    recent_expenses = Expense.objects.order_by('-pk')[:10]
    return render(request, 'home.html', context={'form': new_quick_expense_form, 'recent_expenses': recent_expenses})
