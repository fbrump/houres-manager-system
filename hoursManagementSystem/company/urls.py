from django.urls import path
from .views import index

app = 'company'

urlpatterns = [
    path('', index),
]
