from django.shortcuts import render
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

def list_item(request):
	title = 'List of Books'
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_item.html", context)

def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		"form": form,
		"title": "Add Book",
	}
	return render(request, "add_items.html", context)
