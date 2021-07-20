from django.db import models
from django.db.models.base import Model

# Create your models here.

class Stock(models.Model):
    course = models.CharField(max_length=50, blank=True, null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)
    book_name = models.CharField(max_length=50, blank=True, null=True)
    book_count = models.IntegerField(default='0', blank=True, null=True)
    book_cover = models.ImageField(default='book_cover.jpg')
    index_page = models.ImageField(default='index_page.jpg')
    give_count = models.IntegerField(default='0', blank=True, null=True)
    given_by = models.CharField(max_length=50, blank=True, null=True)
    order_count = models.IntegerField(default='0', blank=True, null=True)
    order_by = models.CharField(max_length=50, blank=True, null=True)
    order_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    alert_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.book_name

