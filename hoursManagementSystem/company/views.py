from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CompanyForm
from .models import Company

def index(request):
    componies = Company.objects.all()[::-1]
    return render(request, 'company/index.html', { 'itens': componies, 'count': len(componies) })

def create(request):
    if request.method == 'POST':
        form_data = CompanyForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponseRedirect(reverse('company:index'))
        else:
            return render(request, 'company/create.html', { 'error_message': form_data.errors })
    return render(request, 'company/create.html')

def delete(request, pk):
    company = Company.objects.get(id=pk)
    if company:
        company.delete()
    return HttpResponseRedirect(reverse('company:index'))
