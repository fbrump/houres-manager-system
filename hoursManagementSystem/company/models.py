from django.db import models

class Company(models.Model):
    """
        Company object to keep all informations about
        args:
            name
            description
            active
            date_create
            date_update
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
