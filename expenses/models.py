from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=64)
    amount = models.FloatField()
    #currency
    date = models.DateField()
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='paid_by')
    added_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='added_by')
    #updated_on
    #updated_by
    #split
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    #receipt
    last_edited = models.DateTimeField(auto_now=True)
    #trail json, in admin?

    def __str__(self):
        return f"{self.name} {self.date}"


class Unit(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=128)
    size = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return f"{self.name} ({self.size}{self.unit.name})"


class ExpenseItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    price = models.FloatField()
    quantity = models.IntegerField()
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    #trail

    def __str__(self):
        return f"{self.item} in {self.expense}"
