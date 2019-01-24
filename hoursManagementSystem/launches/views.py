from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Launch

def index(request):
    return render(request, 'launches/index.html')

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