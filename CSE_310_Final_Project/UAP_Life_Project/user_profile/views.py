from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Promo, PostAd
from .models import Account
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm,CreatePostForm



@login_required
def home(request):
    y = Promo.objects.all()
    xc = PostAd.objects.all().order_by("-date_publish")
    search_term = ""
    if 'search' in request.GET:
        print ("This is working!!!")
        search_term = request.GET['search']
        xc = xc.filter(category__icontains=search_term)

    return render(request, 'user_profile/home.html', {'pro': y, 'AD': xc, 'search_term': search_term})


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
            return render(request, 'user_profile/home.html', {'user': user, 'pro': y, 'AD': xc})
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
                y = Promo.objects.all()
                xc = PostAd.objects.all().order_by("-date_publish")
                return render(request, 'user_profile/home.html', {'user':user,'pro': y, 'AD': xc, 'search_term': search_term})
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
@login_required
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

@login_required
def profile_view(request, user_id):
    profile = get_object_or_404(Account, pk=user_id)
    ads = PostAd.objects.filter(author_id=user_id)
    return render(request, 'user_profile/my_profile.html', {"profile": profile, "ads":ads})


@login_required
def submit_post(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreatePostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreatePostForm()
    context['form'] = form
    return render(request, 'user_profile/submit_post.html', context)

@login_required
def full_post(request, post_id):
    full = get_object_or_404(PostAd, pk=post_id)
    return render(request, 'user_profile/post_detail.html', {'full': full})

