from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from . import forms
from .models import Person, MyModel
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from random import randint
from django.views.generic import TemplateView
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

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

@login_required(login_url='/zaloguj/')
def table(request):
    form = forms.FormName()
    my_dict = {'Title_head': 'Table',
              'people': Person.objects.all()}

    return render(request,'app/people.html', my_dict)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [1, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

class HomeChart(View):
       def get(self, request, *args, **kwargs):
            return render(request, 'app/chart.html', {"customers": 10})