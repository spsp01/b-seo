from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from . import forms
# Create your views here.

def index(request):
    my_dict= {'Title_head': 'Seo Tools | Strona Główna'}
    return render(request,'app/app.html', context=my_dict)

def dane(request):

    form = forms.FormName()
    my_dict = {'Title_head': 'Dane',
              'form': form}

    return render(request,'app/dane.html', my_dict)