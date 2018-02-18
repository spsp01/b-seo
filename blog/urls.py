from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('zaloguj/', views.zaloguj,name='zaloguj'),
    path('zarejestruj/', views.zarejestruj,name='zarejestruj'),
    path('blog/', views.blog,name='blog'),
    path('wyloguj/',views.wyloguj,name='wyloguj'),
    path('faq/',views.Faq.as_view(),name='faq')
]