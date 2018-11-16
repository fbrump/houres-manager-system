from django.test import TestCase

from ..models import Pointsheet
from company.models import Company

class PointSheetsModelTests(TestCase):
	"""docstring for PointSheetsModelTests"""
	def setUp(self):
		self.company = Company.objects.create(name='Company Name')
	def test_create_new_pointsheet_with_success(self):
		values = { 'year': 2001, 'month': 1}
		obj = Pointsheet.objects.create(year=values['year'], month=values['month'], company=self.company)
		self.assertIsNotNone(obj)
		self.assertEqual(values['year'], obj.year)
		self.assertEqual(values['month'], obj.month)
	def test_description_show_for_pointsheets(self):
		year, month = 2001, 3
		expected = '2001 3'
		obj = Pointsheet.objects.create(year=year, month=month, company=self.company)
		self.assertEqual(expected, str(obj))
