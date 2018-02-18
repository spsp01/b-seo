from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from blog.forms import Register
from . import forms
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView

# Create your views here.

class Index(TemplateView):
    #my_dict= {'Title_head': 'Seo Tools | Strona Główna'}
    #return render(request,'index.html', context=my_dict)
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title_head'] = 'Seo Tools | Strona Główna'
        return context

def zaloguj(request):
    my_dict= {'Title_head': 'Zaloguj | Seo Tools'}
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
             login(request,user)
             return HttpResponseRedirect(reverse('app:appindex'))
        else:
            context= {'Title_head': 'Zaloguj | Seo Tools',
                      'Error': 'błąd'}
            return render(request,'login.html',context =context)
    return render(request,'login.html', context=my_dict)


def zarejestruj(request):
    form = forms.Register()

    registered = False

    if request.method == "POST":
        user_form = Register(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.set_password)
            user.save()
            registered = True
    my_dict = {'Title_head': 'Zarejestruj | Seo Tools',
               'register': form,
               'registered': registered}
    return render(request,'zarejestruj.html', context=my_dict)

@login_required
def wyloguj(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def blog(request):
    post_list = Post.objects.all()

    my_dict= {'Title_head': 'Blog | SeoTools',
              'Post': post_list}
    return render(request,'blog.html', context=my_dict)

class Faq(TemplateView):

    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title_head'] = 'FAQ'
        return context