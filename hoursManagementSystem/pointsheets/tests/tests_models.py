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
		expected = '2001 - 3'
		obj = Pointsheet.objects.create(year=year, month=month, company=self.company)
		self.assertEqual(expected, str(obj))

	def test_delete_pointsheet_with_company(self):
		year, month = 2017, 11
		obj = Pointsheet.objects.create(year=year, month=month, company=self.company)
		self.assertIsNotNone(obj)
		self.assertTrue(obj.id > 0)
		pointsheet_id = obj.id
		company_id = self.company.id
		obj.delete()
		seek_company = Company.objects.get(id=company_id)
		self.assertIsNotNone(seek_company)

	def test_delete_company_with_pointsheet(self):
		year, month = 2017, 11
		obj_1 = Pointsheet.objects.create(year=year, month=month, company=self.company)
		year, month = 2017, 12
		obj_2 = Pointsheet.objects.create(year=year, month=month, company=self.company)
		self.assertIsNotNone(obj_1)
		self.assertTrue(obj_1.id > 0)
		pointsheet_id = obj_1.id
		self.company.delete()
		seek_pointsheets = Pointsheet.objects.filter(id=pointsheet_id)
		self.assertTrue(len(seek_pointsheets) == 0)


