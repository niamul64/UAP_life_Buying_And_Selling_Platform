from django.shortcuts import render

# Create your views here.
def Main_page(request):
    return render(request, 'Main_page/Main_page.html')