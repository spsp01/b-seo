from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import forms
from models import Person, MyModel, ProjektUrl, Url, UrlShortner, Clicks
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from random import randint
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
import utils



@login_required(login_url='/zaloguj/')
def dane(request):
    form = forms.FormName()
    my_dict = {'Title_head': 'Dane',
              'form': form}

    return render(request,'app/dane.html', my_dict)
@login_required(login_url='/zaloguj/')
def projekt(request):
    return HttpResponseRedirect('/app/')

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
        qs = Url.objects.values('data_publikacji')
        qlist= list(qs)
        labels = utils.month_date(2,3,2018)
        occur = []
        for i in qlist:
            occur.append(i['data_publikacji'].strftime("%Y-%m-%d"))
        default = []
        for i in labels:
            default.append(occur.count(i))

        #labels = serialize('json', qs)
        default_items = [1, 23, 2, 3, 12, 2]
        data = {
                "labels":  labels,
                "default": default,
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
        context['Title_head'] = 'Panel | Seo Tools'
        context['Person'] = Person.objects.all()
        context['Projekt'] = ProjektUrl.objects.all()
        context['Url'] = Url.objects.all()
        return context

class ProjektView(LoginRequiredMixin, DetailView):
    login_url = '/zaloguj/'
    model = ProjektUrl
    template_name = 'app/project_detail.html'

    qs = Clicks.objects.all().order_by('-date')[0:30]
    dane = list(qs)
    default = {}
    for i in dane:
        default[str(i.date)] = i.clicks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title_head'] = str(ProjektUrl.objects.first())+' Projekt'
        context['Links'] = Url.objects.filter(projekty= context['projekturl'])
        context['Tabela'] =Clicks.objects.all().order_by('-date')[0:30]
        context['Poprzedni'] = Clicks.objects.all().order_by('-date')[0:30]
        context['Poprzedni'] = Clicks.objects.all().order_by('-date')[30:60]
        context['Wykres'] = self.default
        return context

class ShortRedirect(View):
    def get(self,request, pk,*args, **kwargs):
        qs = UrlShortner.objects.filter(shortcode__iexact=pk)
        if qs.count() != 1 and not qs.exists():
            raise Http404("Błąd 404")
        obj = qs.first()
        return HttpResponseRedirect(obj.url)

class ShortURL(View):
    #login_url = '/zaloguj/'

    def get(self,request,*args,**kwargs):
        template_name = 'app/add.html'
        form = forms.SubmitUrlForm()
        context = {
            'Title_head': 'ShortUrl - Generuj Skrólcony URL',
            'form': form
        }
        return render(request,template_name,context=context)


    def post(self, request, *args, **kwargs):
        #print(request.POST.get('url'))
        form = forms.SubmitUrlForm(request.POST)
        context = {
            'Title_head': 'ShortUrl - Generuj Skrólcony URL',
            'form': form
        }
        template_name = 'app/add.html'
        if form.is_valid():
            exist = 0
            new_url = form.clean_urlshort
            obj, created = UrlShortner.objects.get_or_create(url=new_url)
            context_new = {
                'object': obj,
                'created': created,
                'url': new_url,
                'exist': exist
            }
            if created:
                return render(request,'app/add.html', context=context_new)
            else:
                exist= 1
                return render(request, 'app/add.html', context=context_new)

        return render(request, template_name, context= context)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Title_head'] = 'Short | Seo Tools'
    #     return context

def error_404(request):
    data = {}
    return render(request, 'myapp/error_404.html', data)

class URLCreate(LoginRequiredMixin,CreateView):
    login_url = '/zaloguj/'
    model = Url
    form_class = forms.AddUrlForm

class Wykresik(LoginRequiredMixin,TemplateView):
    login_url = '/zaloguj/'
    template_name = 'app/chart3.html'

    # qs = Clicks.objects.all().order_by('-date')[0:30]
    # dane = list(qs)
    # default = {}
    # for i in dane:
    #     default[str(i.date)] = i.clicks
    qs = Url.objects.values('data_publikacji')
    qlist = list(qs)
    labels = utils.month_date(2, 3, 2018)
    occur = []
    for i in qlist:
        occur.append(i['data_publikacji'].strftime("%Y-%m-%d"))
    default = {}
    for i in labels:
        default[str(i)[5:]]= occur.count(i)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.default
        context['Title_head'] = 'Linki dodane | Seo Tools'
        return context


class ProjektList(LoginRequiredMixin,TemplateView):
    login_url = '/zaloguj/'
    template_name = 'app/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title_head'] = 'Lista projektów | Seo Tools'
        context['Projekt'] = ProjektUrl.objects.all()
        return context