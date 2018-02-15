from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def index(request):
    my_dict= {'Title_head': 'Seo Tools | Strona Główna'}
    return render(request,'index.html', context=my_dict)

def zaloguj(request):
    my_dict= {'Title_head': 'Zaloguj | Seo Tools'}
    return render(request,'login.html', context=my_dict)

def zarejestruj(request):
    my_dict= {'Title_head': 'Zarejestruj | Seo Tools'}
    return render(request,'zarejestruj.html', context=my_dict)

def blog(request):
    post_list = Post.objects.all()

    my_dict= {'Title_head': 'Blog | SeoTools',
              'Post': post_list}
    return render(request,'blog.html', context=my_dict)