from django.urls import path, re_path
from app import views


app_name = 'app'
urlpatterns = [
    path('',views.UrlListView.as_view(),name='appindex'),
    path('wykres/', views.Wykresik.as_view(),name='wykres'),
    path('projekt/<int:pk>/', views.ProjektView.as_view(), name='url-detail'),
    path('projekt/', views.projekt, name='projekt'),
    path('projekty/', views.ProjektList.as_view(), name='projekty'),
    path('dane/',views.dane,name='dane'),
    path('url/dodaj/', views.URLCreate.as_view(),name='dodajurl'),
    path('people/', views.table,name='table'),
    path('api/chart/data/', views.ChartData.as_view(), name= 'api-data'),
   # path('wykres/',views.HomeChart.as_view(),name='wykres'),
    #path('dodaj/',views.AddUrl.as_view(),name='dodaj'),
    path('short/',views.ShortURL.as_view(),name='view1'),
    path('short/<pk>/',views.ShortRedirect.as_view(), name='short'),
    #path('lista/', views.UrlListView.as_view(), name='article-list')
    path('tabelka/', views.table,name='my_ajax_url'),

]