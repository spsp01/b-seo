from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name='index'),
    path('zaloguj/', views.zaloguj,name='zaloguj'),
    path('zarejestruj/', views.zarejestruj,name='zarejestruj'),
    path('blog/', views.blog,name='blog')
]