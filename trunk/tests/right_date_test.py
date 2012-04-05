# -*- coding: utf-8 -*-
"""
Тесты модуля определения соответствия даты шаблону
"""


import unittest
import datetime

from church_calendar import right_date

class TestRightDate(unittest.TestCase):
    def testRightDate(self):
        d = right_date.RightDate(datetime.date(2012, 1, 1))
        self.assertTrue(d.isRightDate('01.01'))
        d = right_date.RightDate(datetime.date(2012, 4, 15))
        self.assertTrue(d.isRightDate('E0'))
        d = right_date.RightDate(datetime.date(2012, 1, 21))
        self.assertTrue(d.isRightDate('19.01+01*w6'))
        d = right_date.RightDate(datetime.date(2012, 1, 11))
        self.assertTrue(d.isRightDate('19.01-02*w3'))
        d = right_date.RightDate(datetime.date(2012, 1, 11))
        self.assertTrue(d.isRightDate('10.01:20.01'))
        d = right_date.RightDate(datetime.date(2012, 4, 14))
        self.assertTrue(d.isRightDate('13.04:E0'))
        d = right_date.RightDate(datetime.date(2012, 4, 13))
        self.assertTrue(d.isRightDate('13.04:E0'))
        d = right_date.RightDate(datetime.date(2012, 4, 12))
        self.assertFalse(d.isRightDate('13.04:E0'))
        d = right_date.RightDate(datetime.date(2012, 12, 25))
        self.assertTrue(d.isRightDate('19.12:20.01'))
        d = right_date.RightDate(datetime.date(2012, 1, 2))
        self.assertTrue(d.isRightDate('19.12:20.01'))
        d = right_date.RightDate(datetime.date(2012, 4, 12))
        self.assertFalse(d.isRightDate('13.04:sss'))
        d = right_date.RightDate(datetime.date(2012, 1, 21))
        self.assertTrue(d.isRightDate('19.01~w6'))
        d = right_date.RightDate(datetime.date(2012, 2, 8))
        self.assertTrue(d.isRightDate('w3'))
        d = right_date.RightDate(datetime.date(2012, 2, 8))
        self.assertTrue(d.isRightDate('w3@01.02:10.02@08.02'))

    def testIsStringFitInFormat(self):
        self.assertTrue(right_date.isStringFitInFormat(
                        '19.01', right_date.DATE))
        self.assertTrue(right_date.isStringFitInFormat(
                        'E0', right_date.EASTER))
        self.assertTrue(right_date.isStringFitInFormat(
                        'E-154', right_date.EASTER))
        self.assertTrue(right_date.isStringFitInFormat(
                        '19.01+01*w6', right_date.WEEKDAY_AFTER_DATE))
        self.assertTrue(right_date.isStringFitInFormat(
                        '19.01-11*w1', right_date.WEEKDAY_AFTER_DATE))
        self.assertTrue(right_date.isStringFitInFormat(
                        '19.01~w1', right_date.WEEKDAY_NEAREST_DATE))
        self.assertFalse(right_date.isStringFitInFormat(
                        'aaa', right_date.WEEKDAY_AFTER_DATE))
        self.assertFalse(right_date.isStringFitInFormat(
                        'aaa', right_date.DATE))
        self.assertFalse(right_date.isStringFitInFormat(
                        'aaa', right_date.EASTER))
        self.assertTrue(right_date.isStringFitInFormat(
                        'w1', right_date.WEEKDAY))
        self.assertFalse(right_date.isStringFitInFormat(
                        '19.01-11*w1', right_date.WEEKDAY))

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestRightDate)
unittest.TextTestRunner(verbosity=2).run(suite)
