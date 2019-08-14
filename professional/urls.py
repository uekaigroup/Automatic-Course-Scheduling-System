from django.urls import path
from . import views

app_name='professional'
urlpatterns=[
    path('professional/',views.index,name='index'),
    path('addpro/',views.addpro,name='addpro')
]