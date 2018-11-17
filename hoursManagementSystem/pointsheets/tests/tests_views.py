from django.test import TestCase
from pointsheets.models import Pointsheet, Company

class PointsheetViewsTest(TestCase):
	"""docstring for PointsheetViewsTest"""
	def test_success_pointsheet_index_html(self):
		response = self.client.get('/pointsheets/')
		print(response)
		self.assertEqual(response.status_code, 200)
	def test_success_pointsheet_index_html_filter_year(self):
		year = 2018
		response = self.client.get('/pointsheets/{}/'.format(year))
		self.assertEqual(response.status_code, 200)
	def test_success_pointsheet_index_html_filter_year(self):
		year, month = 2018, 12
		response = self.client.get('/pointsheets/{}/{}/'.format(year, month))
		self.assertEqual(response.status_code, 200)
	def test_success_pointsheet_show_details(self):
		company =  Company.objects.create(name='Company 1')
		pointsheet = Pointsheet.objects.create(year=2000, month=1, company=company)
		pointsheet_id = pointsheet.id
		response = self.client.get('/pointsheets/details/{}/'.format(pointsheet_id))
		self.assertEqual(response.status_code, 200)
