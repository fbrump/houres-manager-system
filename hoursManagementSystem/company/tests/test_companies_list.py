from django.test import TestCase
from datetime import datetime, timezone

from ..models import Company

class CompaniesListTest(TestCase):
    """
        Unittest for list companies
    """
    def setUp(self):
        """
            Set up tests case
        """
        Company.objects.create(name='Sofware Solutions')
    def test_list_one_company_on_list(self):
        """
            Unittest that verify if list companies can list one item on list.
        """
        # arrange
        companies = []
        # act
        companies = Company.objects.all()
        # assert
        self.assertTrue(0 < len(companies))
    def test_list_1000_companies_on_list(self):
        """
            Test if can list 1000 companies on list
        """
        # arrange
        companies = []
        for c in range(0, 1000):
            Company.objects.create(name='Mocke Company {}'.format(c))
        # act
        companies = Company.objects.all()[0:1000]
        # assert
        self.assertTrue(0 < len(companies))
        self.assertEqual(1000, len(companies))
        self.assertTrue('Mocke Company 10' in [item.name for item in companies])
