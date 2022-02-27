from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})


def contactus(request):
    return render(request, 'Contact-Us.html', {})


def aboutus(request):
    return render(request, 'About-Us.html', {})


def menu(request):
    return render(request, 'Our-Menu.html', {})