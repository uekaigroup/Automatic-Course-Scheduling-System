from django.urls import path
from . import views

app_name='classes'
urlpatterns = [
    path('getstage/',views.getstage,name='getstage'),
]