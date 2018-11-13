from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
