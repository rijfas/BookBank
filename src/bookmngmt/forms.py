from django import forms
from django.forms import fields
from .models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['course', 'semester', 'book_name','book_count','book_cover', 'index_page']

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['course', 'semester', 'book_name']

