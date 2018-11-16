from django.db import models

from company.models import Company

class Pointsheet(models.Model):
    """
    Description: Pointsheet
    """
    year = models.IntegerField()
    month = models.IntegerField()
    active = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('year', 'month', 'company')
    def __str__(self):
        return '{} - {}'.format(self.year, self.month)
