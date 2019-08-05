from django.test import TestCase
from django.db import IntegrityError

from ..models import Launch
from company.models import Company
from pointsheets.models import Pointsheet

class LaunchesModelTests(TestCase):
    """
            docstring for LaunchesModelTests
    """
    def setUp(self):
        self.company = Company.objects.create(name='Company Name')
        self.pointsheet = Pointsheet.objects.create(
            year='2018',
            month='01',
            company=self.company)
    
    def test_create_one_launch(self):
        # arrange
        item = Launch(
            date = '2010-01-02',
            time = '09:00',
            pointsheet = self.pointsheet
        )
        # act
        result = Launch.objects.create(
            date = item.date,
            time = item.time,
            pointsheet = item.pointsheet
        )
        items = Launch.objects.filter(id=1)
        # asserts
        self.assertsDefaults(item, result)
        self.assertEqual(1, len(items))
    
    def test_create_two_launch(self):
        # arrange
        item1 = Launch(
            date = '2010-01-02',
            time = '09:00',
            pointsheet = self.pointsheet
        )
        item2 = Launch(
            date = '2010-01-02',
            time = '12:00',
            pointsheet = self.pointsheet
        )
        # act
        result1 = Launch.objects.create(
            date = item1.date,
            time = item1.time,
            pointsheet = item1.pointsheet
        )
        result2 = Launch.objects.create(
            date = item2.date,
            time = item2.time,
            pointsheet = item2.pointsheet
        )
        items = Launch.objects.all()
        # asserts
        self.assertsDefaults(item1, result1)
        self.assertsDefaults(item2, result2)
        self.assertEqual(2, len(items))
    
    def test_create_two_launch_with_equal_date_time_and_pointsheet(self):
        # arrange
        item1 = Launch(
            date = '2010-01-02',
            time = '09:00',
            pointsheet = self.pointsheet
        )
        item2 = Launch(
            date = '2010-01-02',
            time = '09:00',
            pointsheet = self.pointsheet
        )
        # act
        result1 = Launch.objects.create(
            date = item1.date,
            time = item1.time,
            pointsheet = item1.pointsheet
        )
        with self.assertRaises(Exception) as context:
            Launch.objects.create(
                date = item2.date,
                time = item2.time,
                pointsheet = item2.pointsheet
            )
        # asserts
        self.assertIsNotNone(context)
        self.addTypeEqualityFunc(type(IntegrityError), type(context))
    
    def test_active_one_launch_that_was_created(self):
        # arrange
        item1 = Launch(
            date = '2010-01-02',
            time = '09:00',
            pointsheet = self.pointsheet
        )
        result1 = Launch.objects.create(
            date = item1.date,
            time = item1.time,
            pointsheet = item1.pointsheet
        )
        # act
        result1.active = True
        result1.save()
        itemCreated = Launch.objects.get(id=result1.id)
        # asserts
        self.assertIsNotNone(itemCreated)
        self.assertTrue(itemCreated.active)
    
    def test_deactivate_one_launch_that_was_created(self):
        # arrange
        item1 = Launch(
            date = '2010-01-02',
            time = '09:00',
            pointsheet = self.pointsheet
        )
        result1 = Launch.objects.create(
            date = item1.date,
            time = item1.time,
            pointsheet = item1.pointsheet
        )
        # act
        result1.active = False
        result1.save()
        itemCreated = Launch.objects.get(id=result1.id)
        # asserts
        self.assertIsNotNone(itemCreated)
        self.assertFalse(itemCreated.active)
    
    def test_create_one_item_then_deactivate_and_create_other_with_same_values_raise_exception(self):
        # arrange
        item1 = Launch(
            date = '2010-01-02',
            time = '09:00',
            pointsheet = self.pointsheet
        )
        result1 = Launch.objects.create(
            date = item1.date,
            time = item1.time,
            pointsheet = item1.pointsheet
        )
        result1.active = False
        result1.save()
        # act
        with self.assertRaises(Exception) as context:
            result2 = Launch.objects.create(
                date = item1.date,
                time = item1.time,
                pointsheet = item1.pointsheet
            )
        # asserts
        self.assertIsNotNone(context)
        self.addTypeEqualityFunc(type(IntegrityError), type(context))
    
    def assertsDefaults(self, item, result):
        self.assertEqual(item.date, result.date)
        self.assertEqual(item.time, result.time)
        self.assertTrue(item.active)
        self.assertIsNotNone(result.id)
        self.assertGreater(result.id, 0)
        self.assertIsNotNone(result.date_create)


