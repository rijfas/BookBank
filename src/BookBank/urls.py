"""BookBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookmngmt import views

urlpatterns = [
    path('', views.site, name='site'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('list_items/', views.list_items, name='list_items'),
    path('add_item/', views.add_item, name='add_item'),
    path('update_item/<str:pk>/', views.update_item, name="update_item"),
    path('delete_item/<str:pk>/', views.delete_item, name="delete_item"),
    path('book_details/<str:pk>/', views.book_details, name="book_details"),
    path('order_book/<str:pk>/', views.order_book, name="order_book"),
    path('add_book/<str:pk>/', views.add_book, name="add_book"),
    path('alert_level/<str:pk>/', views.alert_level, name="alert_level"),
    path('donate_book/', views.donate_book, name='donate_book'),
    path('list_history/', views.list_history, name='list_history'),
]
