from dataclasses import field
from pyexpat import model
from django.db import models

# Create your models here.
class IncomeAmount(models.Model):
    INCOME_CATEGORIES = (
        ('salary', 'Salary'),
        ('contract_hustles', 'Contract Gig'),
        ('one-time-gig', 'One Time Gig'),
        ('gifted', 'Allowance'),
    )
    name=models.CharField(max_length=100,choices=INCOME_CATEGORIES)
    date_received=models.DateField()
    amt=models.IntegerField()
    
class Expense(models.Model):
    EXPENSE_CATEGORIES = (
        ('clothing', 'Clothing'),
        ('footwear', 'Foot Wear'),
        ('transport', 'Transport'),
        ('savings', 'Savings'),
        ('debtpayment', 'Paying Debts'),
        ('beddings', 'Beddings'),
        ('furniture', 'Furniture'),
        ('electronics', 'Electronics'),
        ('entertainment', 'Entertainment'),
        ('households', 'Households'),
    )
    name=models.CharField(max_length=150)
    item_category=models.CharField(max_length=100,choices=EXPENSE_CATEGORIES)
    price=models.FloatField()
    purchase_date=models.DateField()
    