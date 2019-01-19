from django.test import TestCase

from ..models import Launch
from company.models import Company
from pointsheets.models import Pointsheet

class LaunchesModelTests(TestCase):
    """
            docstring for LaunchesModelTests
    """
    def setUp(self):
        self.company = Company.objects.create(name='Company Name')
        pointsheet = Pointsheet.objects.create(
            year='2018',
            month='01',
            company=self.company)
    def test_create_new_launche():
        pass

