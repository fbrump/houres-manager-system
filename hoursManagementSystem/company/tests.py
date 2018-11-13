from django.test import TestCase

from .models import Company

class CompaniesListTest(TestCase):
    """
        Unittest for list companies
    """
    def setup(self):
        Company.objects.create(name='Sofware Solutions')
    def test_list_one_company_on_list(self):
        # arrange
        companies = []
        # act
        # assert
        self.assertEqual(1, len(companies))

