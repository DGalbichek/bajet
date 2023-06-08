from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from expenses.forms import NewQuickExpenseForm
from expenses.models import Expense


@login_required
def home_page(request):
    new_quick_expense_form = NewQuickExpenseForm(data=request.POST if request.POST else None,
                                                 initial={'paid_by': request.user})

    if request.POST and new_quick_expense_form.is_valid():
        new_quick_expense_form.save()
        new_quick_expense_form = NewQuickExpenseForm()

    recent_expenses = Expense.objects.order_by('-last_edited')[:10]
    return render(request, 'home.html', context={'form': new_quick_expense_form, 'recent_expenses': recent_expenses})
