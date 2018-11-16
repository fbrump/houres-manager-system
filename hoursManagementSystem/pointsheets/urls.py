# pointsheets/urls.py

from django.urls import path
from . import views

app_name = 'pointsheets'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>', views.index, name='index-year'),
    path('<int:year>/<int:month>/', views.PointsheetListView.as_view(), name='index-year-month'),
]
