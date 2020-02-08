from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question, Answer
from user_profile.models import Account
from .forms import CreateQuestionForm, CreateAnswerForm

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


def submit_answer(request, question_id):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateAnswerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.question = Question.objects.get(pk=question_id)
        obj.save()
        form = CreateAnswerForm()
    context['form'] = form
    return render(request, 'question_bank/submit_answer.html', context)


def full_answer(request, answer_id):
    full = get_object_or_404(Answer, pk=answer_id)
    return render(request, 'question_bank/full_answer.html', {'full': full})


def browse_question(request):
    questions = Question.objects
    return render(request, 'question_bank/browse_question.html', {'questions': questions})


def full_question(request, question_id):
    full = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question_id=question_id)
    return render(request, 'question_bank/full_question.html', {"full": full, 'answers': answers})
