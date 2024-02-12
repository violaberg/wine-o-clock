from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_cellar(request):
    return HttpResponse("It's wine o'clock somewhere!")
