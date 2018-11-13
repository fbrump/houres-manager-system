from django.urls import path
from .views import index, create

app_name = 'company'

urlpatterns = [
    path('', index, name='index'),
    path('new/', create, name='create'),
]
