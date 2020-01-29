from django.shortcuts import render, redirect, reverse
from user_profile.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def home(request):
    return render(request, 'user_profile/Main_page.html')


def index(request):
    return render(request, 'user_profile/index.html')


def loginpage(request):
    return render(request, 'user_profile/login.html')


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()                 # saving to database
            user.set_password(user.password)        # hashing the password
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user                     # one to one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'user_profile/signup.html',
                           {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered': registered})

# log in view


def user_login(request):
    if request.method == 'POST':
        given_username = request.POST.get('username')
        given_password = request.POST.get('password')
        user = authenticate(username=given_username, password=given_password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'user_profile/Main_page.html')
            else:
                return HttpResponse('Account not active!!')
        else:
            return HttpResponse("Invalid login information!!")

    else:
        return render(request, 'user_profile/login.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'user_profile/index.html')