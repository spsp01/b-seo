from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def index(request):
    my_dict= {'Title_head': 'Seo Tools | Strona Główna'}
    return render(request,'app/app.html', context=my_dict)