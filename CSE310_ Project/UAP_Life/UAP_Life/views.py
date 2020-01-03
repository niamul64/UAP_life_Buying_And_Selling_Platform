from django.http import HttpResponse
from django.shortcuts import render


def Home_Page(request):
    return render(request, 'home.html')


def Main_Page(request):
    return render(request, 'main_page.html')