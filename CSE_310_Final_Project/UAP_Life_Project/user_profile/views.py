from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Promo, PostAd
from .models import Account
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


@login_required
@login_required
def home(request):
    y = Promo.objects.all()

    xc = PostAd.objects.all().order_by("-date_publish")

    if request.method == 'POST':
        se= request.POST["search"]
        print ("got form SEarch:"+se)
        res= [x for x in xc if se in x.title]
        xc=res

    return render(request, 'user_profile/Main_page.html',{'pro':y,'AD':xc})


def index(request):
    return render(request, 'user_profile/index.html')


def loginpage(request):
    return render(request, 'user_profile/login.html')


def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            y = Promo.objects.all()
            #print (y)
            xc = PostAd.objects.all().order_by("-date_publish")
            #print (xc)
            return render(request, 'user_profile/Main_page.html', {'user': user, 'pro': y, 'AD': xc})
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
    y = Promo.objects.all
    return render(request, 'user_profile/login.html',context,{'promos':y})



@login_required
def user_logout(request):
    logout(request)
    return render(request, 'user_profile/index.html')


# user profile update

def profile_update(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context ={}
    if request.POST:
        form = AccountUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={

                "username": request.user.username,
                "profile_pic": request.user.profile_pic,
            }
        )

    context['update_form'] = form
    return render(request, 'user_profile/profile_update.html', context)


def profile_view(request, user_id):
    profile = get_object_or_404(Account, pk=user_id)
    print(profile)
    return render(request, 'user_profile/my_profile.html', {"profile": profile})

