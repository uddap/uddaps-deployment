# Create your views here.
from django.shortcuts import render
#
# def home(request):
#     return render(request, 'home.html')
from django.contrib import admin
from django.urls import path, include
from views import item_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('', include('myapp.urls')),
    path('', item_list, name='item_list'),]

# views.py
from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

