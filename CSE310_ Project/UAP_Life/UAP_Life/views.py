from django.http import HttpResponse
from django.shortcuts import render


def Home_Page(request):
    return render(request, 'index.html')
def Main_Page(request):
    return render(request, 'main_home_page.html')
def post_ad(request):
    return render(request, 'post_ad_1.html')
def post_ad2(request):
    return render(request, 'post_ad_2.html')
def question_bank(request):
    return render(request,'questionbank_first_page.html')
def submit_question(request):
    return render(request,'submit_question_page.html')