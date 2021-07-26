from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import csv
from .models import Stock
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm

# Create your views here.

def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def site(request):
	title = 'Welcome: This is the Site Page'
	context = {
	"title": title,
	}
	return render(request, "site.html",context)

def list_items(request):
	header = 'List of Books'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"header": header,
		"queryset": queryset,
		"form": form,
	}
	if request.method == 'POST':
		queryset = Stock.objects.filter(
			#course__icontains=form['course'].value(),
			semester__icontains=form['semester'].value(),
			book_name__icontains=form['book_name'].value()
			)
		context = {
					"form": form,
					"header": header,
					"queryset": queryset,
		}
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
			writer = csv.writer(response)
			writer.writerow(['COURSE', 'SEMESTER', 'BOOK_NAME'])
			instance = queryset
			for stock in instance:
				writer.writerow([stock.course, stock.semester, stock.book_name])
			return response

	return render(request, "list_items.html", context)

def add_item(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/list_items')
	context = {
		"form": form,
		"title": "Add Book",
	}
	return render(request, "add_item.html", context)

def update_item(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Saved')
			return redirect('/list_items')
	context = {
		'form':form
	}
	return render(request, 'add_item.html', context)

def delete_item(request, pk):
	queryset = Stock.objects.get(id=pk)
	book_name = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Successfully Deleted')
		return redirect('/list_items')
	context = {
		'book_name':book_name
	}
	return render(request, 'delete_item.html', context)
