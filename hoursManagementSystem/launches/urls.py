# pointsheets/urls.py

from django.urls import path
from . import views

app_name = 'launches'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.LauncheCreateView.as_view(), name='create'),
]
