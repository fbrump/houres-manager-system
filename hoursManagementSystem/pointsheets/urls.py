# pointsheets/urls.py

from django.urls import path
from . import views

app_name = 'pointsheets'

urlpatterns = [
    path('', views.PointsheetListView.as_view(), name='index'),
    path('<int:year>/', views.PointsheetListView.as_view(), name='index-year'),
    path('<int:year>/<int:month>/', views.PointsheetListView.as_view(), name='index-year-month'),
    path('details/<int:pk>/', views.PointsheetsDetailsView.as_view(), name='details'),
    path('create/', views.PointsheetCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.PointsheetDeleteView.as_view(), name='delete'),
]
