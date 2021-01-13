from django.urls import path
from . import views

app_name = 'calendar'
urlpatterns = [
    path('', views.index, name='index'),
]