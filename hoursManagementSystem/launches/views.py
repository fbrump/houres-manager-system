from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Launch

class LauncheCreateView(CreateView):
    """
        docstring for LauncheCreateView
    """
    model = Launch
    fields = ['date', 'time', 'pointsheet']
    template_name = 'launches/create.html'
    success_url = reverse_lazy('launches:index')
    def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

class LauncheListView(ListView):
    """
        docstring for LauncheListView
    """
    model = Launch
    paginated_by = 100
    template_name = 'launches/index.html'
    def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    print(context)
	    return context
