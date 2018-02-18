from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from . import forms

from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/zaloguj/')
def index(request):
    my_dict= {'Title_head': 'Seo Tools | Strona Główna'}
    return render(request,'app/app.html', context=my_dict)

@login_required(login_url='/zaloguj/')
def dane(request):
    form = forms.FormName()
    my_dict = {'Title_head': 'Dane',
              'form': form}

    return render(request,'app/dane.html', my_dict)