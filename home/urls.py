# from django.contrib import admin
from django.urls import path
from . import views

app_name='home'
urlpatterns=[
    path('home<id>/',views.home,name='home'),
    path('ordercla/',views.ordercla,name='ordercla'),
    path('getcourse/<id>/',views.getcourse,name='getcourse'),
    path('changecourse/<id>/',views.changecourse,name='changecourse')
]