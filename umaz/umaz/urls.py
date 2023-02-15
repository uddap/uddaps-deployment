"""umaz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# Add the allauth URLs to your project:In your urls.py file, add the following to include the allauth URLs:
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'umazapp/', include('umazapp.urls')),
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
# from umaz.umazapp import views
#
# urlpatterns = [
#     path('', views.homepage, name='homepage'),
#     path('admin/', admin.site.urls),
#     path('umazapp/', include('umaz.umazapp.urls')),
# ]

