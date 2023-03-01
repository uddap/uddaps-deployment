# from django.shortcuts import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('HomePuhfghfghfghpppp')
    return render(request, 'home.html')
