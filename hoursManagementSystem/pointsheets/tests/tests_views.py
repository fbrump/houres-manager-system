from django.test import TestCase

class PointsheetViewsTest(TestCase):
	"""docstring for PointsheetViewsTest"""
	def test_success_pointsheet_index_html(self):
		response = self.client.get('/pointsheets/')
		print(response)
		self.assertEqual(response.status_code, 200)
	def test_success_pointsheet_index_html_filter_year(self):
		year = 2018
		response = self.client.get('/pointsheets/{}/'.format(year))
		print(response)
		self.assertEqual(response.status_code, 200)
