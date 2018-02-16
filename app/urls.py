from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='app'),
    path('dane/',views.dane,name='dane'),
]