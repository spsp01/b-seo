from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('',views.Index.as_view(),name='appindex'),
    path('dane/',views.dane,name='dane'),
    path('people/', views.table,name='table'),
    path('api/chart/data/', views.ChartData.as_view(), name= 'api-data'),
    path('wykres/',views.HomeChart.as_view(),name='wykres'),
    path('dodaj/',views.AddUrl.as_view(),name='dodaj'),
    path('lista/', views.UrlListView.as_view(), name='article-list')
    # path('tabelka/', views.LineChartJSONView,name='my_ajax_url'),

]