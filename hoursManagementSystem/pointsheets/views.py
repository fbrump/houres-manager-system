from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import Pointsheet


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
	ordering = ['-year', '-month']

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

class PointsheetCreateView(CreateView):
	"""docstring for PointsheetCreateView"""
	model = Pointsheet
	fields = ['year', 'month', 'company']
	# template_name_suffix = '/create'
	template_name = 'pointsheets/create.html'
	success_url = reverse_lazy('pointsheets:index')
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

class PointsheetDeleteView(DeleteView):
    model = Pointsheet
    # template_name = "pointsheets/confirm_delete.html"
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy('pointsheets:index')

class PointsheetUpdateView(UpdateView):
	model = Pointsheet
	template_name_suffix = "_update"
	success_url = reverse_lazy('pointsheets:index')
	fields = ['year', 'month', 'company']
