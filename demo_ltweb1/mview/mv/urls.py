from django.urls import path
from . import views

app_name = 'mv'
urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('mv/', views.listMv, name='list-mv'),
    path('detail-mv/', views.detailMV, name='detail-mv'),
]
