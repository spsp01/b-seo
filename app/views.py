from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from . import forms
from .models import Person, MyModel, ProjektUrl, Url
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from random import randint
from django.views.generic import TemplateView, View, ListView, DetailView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Index(LoginRequiredMixin,TemplateView):

    login_url = '/zaloguj/'
    template_name = 'app/app.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title_head'] = 'Panel | Seo Tools'
        return context

class AddUrl(LoginRequiredMixin,TemplateView):
    login_url = '/zaloguj/'
    template_name = 'app/add.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title_head'] = 'Dodaj | Seo Tools'
        return context


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

class UrlListView(LoginRequiredMixin,ListView):
    login_url = '/zaloguj/'
    template_name = "app/app.html"
    model = ProjektUrl
    context_object_name = "adresy_url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Person'] = Person.objects.all()
        context['Projekt'] = ProjektUrl.objects.all()
        return context

class ProjektView(LoginRequiredMixin, DetailView):
    login_url = '/zaloguj/'
    model = ProjektUrl
    template_name = 'app/project_detail.html'
    #pk_url_kwarg = 'urlpk'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title_head'] = 'Title'
        return context

class ShortRedirect(View):

    name = 'asdasdasd'
    def get(self,request,*args, **kwargs):
        print(*args)
        print(**kwargs)
        return HttpResponse('Hello again')