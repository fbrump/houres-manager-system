from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Pointsheet

def index(request):
	return render(request, 'pointsheets/index.html')

class PointsheetsDetailsView(DetailView):
	model = Pointsheet

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

class PointsheetListView(ListView):
	model = Pointsheet
	paginated_by = 100

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context
