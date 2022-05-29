import imp
from django.forms import ModelForm
from ..models import Expense,IncomeAmount

class IncomeForm(ModelForm):
    class Meta:
        model=IncomeAmount
        fields = ['name','date_received','amt']

class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        fields=['name','item_category','price','purchase_date']
    