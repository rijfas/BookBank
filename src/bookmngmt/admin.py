from django.contrib import admin
from .models import Course, Stock, Donation
from .forms import StockCreateForm

# Register your models here.

class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['course', 'semester', 'book_name', 'book_count']
    form = StockCreateForm
    list_filter = ['course','semester']
    search_fields = ['course', 'semester', 'book_name']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Course)
admin.site.register(Donation)