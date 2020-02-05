from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm
from .models import Promo
@login_required
def home(request):
    y = Promo.objects.all()
    print (y)
    return render(request, 'user_profile/Main_page.html', {'pro': y})


def index(request):
    return render(request, 'user_profile/index.html')


def loginpage(request):
    return render(request, 'user_profile/login.html')


def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email,password=raw_password)
            login(request, user)
            return render(request,'user_profile/Main_page.html',{'user':user})
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'user_profile/signup.html',context)


# log in view


def log_in(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)
            if user:
                login(request,user)
                return render(request,'user_profile/Main_page.html',{'user':user})
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user_profile/login.html',context)



@login_required
def user_logout(request):
    logout(request)
    return render(request, 'user_profile/index.html')


