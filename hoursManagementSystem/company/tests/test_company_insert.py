from django.test import TestCase
from datetime import datetime, timezone

from ..models import Company

class CompanyInsertTest(TestCase):
    """
        Company insert tests
    """
    def setUp(self):
        pass
    def test_crate_new_company(self):
        # arrange
        date_now = datetime.now(timezone.utc) # datetime.today().now()
        data = {
            'name': 'Pinter&T',
            'description': 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.'
        }
        # act
        new_company = Company.objects.create(
            name=data['name'],
            description=data['description']
            )
        # assert
        self.assertIsNotNone(new_company)
        self.assertIsNotNone(new_company.id)
        self.assertTrue(new_company.id > 0)
        self.assertNotEqual(date_now, new_company)
        self.assertIsNotNone(new_company.date_create)
        self.assertTrue(date_now < new_company.date_create)
        self.assertEqual(data['name'], new_company.name)
        self.assertEqual(data['description'], new_company.description)
    def test_crate_new_company_without_description(self):
        # arrange
        date_now = datetime.now(timezone.utc) # datetime.today().now()
        data = {
            'name': 'Pinter&T',
        }
        # act
        new_company = Company.objects.create(
            name=data['name'],
            )
        # assert
        self.assertIsNotNone(new_company)
        self.assertIsNotNone(new_company.id)
        self.assertTrue(new_company.id > 0)
        self.assertNotEqual(date_now, new_company)
        self.assertIsNotNone(new_company.date_create)
        self.assertTrue(date_now < new_company.date_create)
        self.assertEqual(data['name'], new_company.name)
