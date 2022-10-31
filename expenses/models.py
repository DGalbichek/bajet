from django.db import models


class Expense(models.Model):
    name = models.CharField(max_length=64)
    amount = models.FloatField()
    #currency
    date = models.DateField()
    #paid by
    #split
    #category
    #receipt
    last_edited = models.DateTimeField(auto_now=True)
    #trail json, in admin?
