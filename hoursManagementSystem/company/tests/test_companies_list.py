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
        # arrange
        companies = []
        # act
        companies = Company.objects.all()
        # assert
        self.assertTrue(0 < len(companies))
