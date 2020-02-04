from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question
from user_profile.models import Account
from .forms import CreateQuestionForm
# Create your views here.


def q_index(request):
    return render(request,'question_bank/q_index.html')


def must_authenticate(request):
    return render(request, 'question_bank/must_authenticate.html')


def submit_question(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateQuestionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateQuestionForm()
    context['form'] = form
    return render(request, 'question_bank/submit_question.html', context)


def browse_question(request):
    questions = Question.objects
    return render(request,'question_bank/browse_question.html',{'questions': questions})