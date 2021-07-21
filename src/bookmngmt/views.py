from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockCreateForm

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
	queryset = Stock.objects.all()
	context = {
		"header": header,
		"queryset": queryset,
	}
	return render(request, "list_items.html", context)

def add_item(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/list_items')
	context = {
		"form": form,
		"title": "Add Book",
	}
	return render(request, "add_item.html", context)
