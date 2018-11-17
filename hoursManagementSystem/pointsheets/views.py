from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


from .models import Pointsheet

# def index(request):
# 	return render(request, 'pointsheets/index.html')

class PointsheetsDetailsView(DetailView):
	model = Pointsheet
	template_name = 'pointsheets/details.html'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

class PointsheetListView(ListView):
	model = Pointsheet
	paginated_by = 100
	template_name = 'pointsheets/index.html'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

class PointsheetCreateView(CreateView):
	"""docstring for PointsheetCreateView"""
	model = Pointsheet
	fields = ['year', 'month', 'company']
	# template_name_suffix = '/create'
	template_name = 'pointsheets/create.html'

