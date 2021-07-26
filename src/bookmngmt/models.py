from django.db import models
from django.db.models.base import Model

# Create your models here.

semester_choice = (
		('UG 1', 'UG 1'),('UG 2', 'UG 2'),('UG 3', 'UG 3'),('UG 4', 'UG 4'),
        ('UG 5', 'UG 5'),('UG 6', 'UG 6'),('PG 1', 'PG 1'),('PG 2', 'PG 2'),
        ('PG 3', 'PG 3'),('PG 4', 'PG 4'),
	)

class Course(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True, default=None)
	def __str__(self):
		return self.name

class Stock(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    semester = models.CharField(max_length=20, blank=True, null=True, choices=semester_choice)
    book_name = models.CharField(max_length=50, blank=True, null=True)
    book_count = models.IntegerField(default='0', blank=True, null=True)
    book_cover = models.ImageField(default='book_cover.jpg')
    index_page = models.ImageField(default='index_page.jpg')
    add_count = models.IntegerField(default='0', blank=True, null=True)
    add_by = models.CharField(max_length=50, blank=True, null=True)
    order_count = models.IntegerField(default='0', blank=True, null=True)
    order_by = models.CharField(max_length=50, blank=True, null=True)
    order_to = models.CharField(max_length=50, blank=True, null=True)
    student_details = models.TextField()
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    alert_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.book_name

