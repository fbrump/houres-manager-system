from django.forms import ModelForm, BooleanField

from .models import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'active',]

