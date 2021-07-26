from django import forms
from django.forms import fields
from .models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['course', 'semester', 'book_name','book_count','book_cover', 'index_page']
    def clean_course(self):
        course = self.cleaned_data.get('course')
        if not course:
            raise forms.ValidationError('This field is required')
        return course
    def clean_semester(self):
        semester = self.cleaned_data.get('semester')
        if not semester:
            raise forms.ValidationError('This field is required')
        return semester
    def clean_book_name(self):
        book_name = self.cleaned_data.get('book_name')
        if not book_name:
            raise forms.ValidationError('This field is required')
        for instance in Stock.objects.all():
            if instance.book_name == book_name:
                raise forms.ValidationError(str(book_name) + ' is already added')
        return book_name

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['course', 'semester', 'book_name']

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['course', 'semester', 'book_name','book_count','book_cover', 'index_page']

class OrderForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['order_count', 'order_to']


class AddForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['add_count']

