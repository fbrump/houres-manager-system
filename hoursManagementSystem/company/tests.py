from django.test import TestCase

class CompaniesListTest(TestCase):
    def test_list_one_company_on_list(self):
        # arrange
        companies = []
        # act
        # assert
        self.assertEqual(1, len(companies))

