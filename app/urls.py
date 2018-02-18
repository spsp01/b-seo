from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('',views.index,name='appindex'),
    path('dane/',views.dane,name='dane')
]