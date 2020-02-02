from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm

@login_required
def home(request):
    return render(request, 'user_profile/Main_page.html')


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
            account = authenticate(email=email,password=raw_password)
            login(request, account)
            return redirect('home')
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
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user_profile/login.html',context)



@login_required
def user_logout(request):
    logout(request)
    return render(request, 'user_profile/index.html')


@login_required
def my_profile(request, profile_username):
    profile_detail = get_object_or_404(UserProfileInfo, pk=profile_username)
    print(type(profile_detail))
    print(profile_detail)
    return render(request, 'user_profile/my_profile.html', {'profile_detail': profile_detail})
