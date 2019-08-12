from django.urls import path
from . import views

app_name='classes'
urlpatterns = [
    path('',views.index,name='classes'),
]