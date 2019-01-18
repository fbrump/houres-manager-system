from django.db import models

from pointsheets.models import Pointsheet

class Launche(models.Model):
    """
        Description: Launche
        fields:
            date
            time
            active
            date_create
            date_update
            pointsheet
    """
    date = models.DateField()
    time = models.TimeField()
    active = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    pointsheet = models.ForeignKey(Pointsheet, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'time', 'pointsheet')
    def __str__(self):
        return '{} - {}'.format(self.date, self.time)

