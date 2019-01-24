from django.test import TestCase

from company.models import Company
from pointsheets.models import Pointsheet
from ..models import Launch

class LaunchViewsTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Company Name')
        self.pointsheet = Pointsheet.objects.create(
            year='2018',
            month='01',
            company=self.company
        )
    def test_success_create_new_launch(self):
        data = {
            'date': '2010-01-02',
            'time': '09:00',
            'pointsheet_id': self.pointsheet.id
        }
        response = self.client.post('launches/', data=data)
        self.assertEqual(response.status_code, 201)
