from django.contrib import admin

from expenses.models import Category, Expense, Item, ExpenseItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'paid_by')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ExpenseItem)
class ExpenseItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'unit_price', 'quantity', 'expense')
