from django.test import TestCase

class PointsheetViewsTest(TestCase):
	"""docstring for PointsheetViewsTest"""
	def test_success_pointsheet_index_html(self):
		response = self.client.get('/pointsheets/')
		print(response)
		self.assertEqual(response.status_code, 200)
