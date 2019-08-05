# pointsheets/urls.py

from django.urls import path
from . import views

app_name = 'launches'

urlpatterns = [
    path('', views.LauncheListView.as_view(), name='index'),
    path('create/', views.LauncheCreateView.as_view(), name='create'),
    path('active/<int:pk>/', views.LaunchActiveView.as_view(), name='active'),
]
