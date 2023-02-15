# from django.conf.urls import url
# from umazapp import views
# from .views import appurlinfo
# from .views import facebook_login
#
# # Add a URL pattern to your urls.py file to handle the Facebook login process:
# urlpatterns = [
#     url(r'test/', views.umazapp),
#     url('facebook_login/', facebook_login, name='facebook_login'),
# ]

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^home/', views.home),
    re_path(r'^register/', views.register),
]

# WARNINGS:
# ?: (2_0.W001) Your URL pattern 'umazapp/$' has a route that contains '(?P<', begins with a '^', or ends with a '$'. This was likely a
# n oversight when migrating to django.urls.path().
#
# System check identified 1 issue (0 silenced).
# February 15, 2023 - 12:00:22
# Django version 4.1.7, using settings 'umaz.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
# Page not found (404)
# Request Method:	GET
# Request URL:	http://127.0.0.1:8000/
# Using the URLconf defined in umaz.urls, Django tried these URL patterns, in this order:
#
# admin/
# umazapp/$
# The empty path didn’t match any of these.
#
# You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.

# from django.urls import include, path
# from django.contrib import admin
# from . import views
#
# urlpatterns = [
#     path('', views.homepage, name='homepage'),
#     path('admin/', admin.site.urls),
#     path('umazapp/', include('umaz.umazapp.urls')),
# ]
