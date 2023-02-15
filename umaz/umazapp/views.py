from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from facebook import GraphAPI

# Create your views here.
# def homepage(request):
#     return render(request, 'home.html')

def home(request):
    return render(request, 'umazapp/home.html')

def register(request):
    registered = False
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'umazapp/register.html', {'form': form})

#
# def appurlinfo(request):
#     s='<h1>Application Level urls Demo</h1>'
#     return HttpResponse(s)
#
#
# # In your Django views, use the following code to handle the Facebook login process:
# def facebook_login(request):
#     code = request.GET.get('code')
#     if code:
#         graph = GraphAPI(access_token=code, version="3.0")
#         profile = graph.get_object("/me")
#         return HttpResponse(profile)
#     #     # Use the profile data to log in or create a user in your database
#     #     # ...
#     #     return redirect('your_redirect_url')
#     # else:
#     #     return redirect('https://www.facebook.com/v3.0/dialog/oauth?client_id={}&redirect_uri={}'.format(
#     #         FACEBOOK_APP_ID,
#     #         'your_redirect_uri'
#     #     ))
