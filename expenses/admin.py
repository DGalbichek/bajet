from django.contrib import admin

from expenses.models import Category, Expense, Unit, Item, ExpenseItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ExpenseItemInlineAdmin(admin.TabularInline):
    model = ExpenseItem
    extra = 0


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'paid_by', 'category')
    list_filter = ('category__name', 'paid_by__username', 'added_by__username')
    search_field = ('name', )

    inlines = (ExpenseItemInlineAdmin, )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'unit')
    list_filter = ('unit__name', )
    search_field = ('name', )


@admin.register(ExpenseItem)
class ExpenseItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'quantity', 'expense')
