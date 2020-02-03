from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.


def q_index(request):
    return render(request,'question_bank/q_index.html')
