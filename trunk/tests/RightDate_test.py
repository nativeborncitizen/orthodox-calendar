# -*- coding: utf-8 -*-
"""
Тесты модуля определения соответствия даты шаблону
"""


import unittest
import datetime

import RightDate

class TestRightDate(unittest.TestCase):
    def testRightDate(self):
        d = RightDate.RightDate(datetime.date(2012, 1, 1))
        self.assertTrue(d.isRightDate('01.01'))
        d = RightDate.RightDate(datetime.date(2012, 4, 15))
        self.assertTrue(d.isRightDate('E0'))
        d = RightDate.RightDate(datetime.date(2012, 1, 21))
        self.assertTrue(d.isRightDate('19.01+01*w6'))
        d = RightDate.RightDate(datetime.date(2012, 1, 11))
        self.assertTrue(d.isRightDate('19.01-02*w3'))
        d = RightDate.RightDate(datetime.date(2012, 1, 11))
        self.assertTrue(d.isRightDate('10.01:20.01'))
        d = RightDate.RightDate(datetime.date(2012, 4, 14))
        self.assertTrue(d.isRightDate('13.04:E0'))
        d = RightDate.RightDate(datetime.date(2012, 4, 13))
        self.assertTrue(d.isRightDate('13.04:E0'))
        d = RightDate.RightDate(datetime.date(2012, 4, 12))
        self.assertFalse(d.isRightDate('13.04:E0'))
        d = RightDate.RightDate(datetime.date(2012, 12, 25))
        self.assertTrue(d.isRightDate('19.12:20.01'))
        d = RightDate.RightDate(datetime.date(2012, 1, 2))
        self.assertTrue(d.isRightDate('19.12:20.01'))
        d = RightDate.RightDate(datetime.date(2012, 4, 12))
        self.assertFalse(d.isRightDate('13.04:sss'))
        d = RightDate.RightDate(datetime.date(2012, 1, 21))
        self.assertTrue(d.isRightDate('19.01~w6'))
        d = RightDate.RightDate(datetime.date(2012, 2, 8))
        self.assertTrue(d.isRightDate('w3'))
        d = RightDate.RightDate(datetime.date(2012, 2, 8))
        self.assertTrue(d.isRightDate('w3@01.02:10.02@08.02'))

    def testIsStringFitInFormat(self):
        self.assertTrue(RightDate.isStringFitInFormat(
                        '19.01', RightDate.DATE))
        self.assertTrue(RightDate.isStringFitInFormat(
                        'E0', RightDate.EASTER))
        self.assertTrue(RightDate.isStringFitInFormat(
                        'E-154', RightDate.EASTER))
        self.assertTrue(RightDate.isStringFitInFormat(
                        '19.01+01*w6', RightDate.WEEKDAY_AFTER_DATE))
        self.assertTrue(RightDate.isStringFitInFormat(
                        '19.01-11*w1', RightDate.WEEKDAY_AFTER_DATE))
        self.assertTrue(RightDate.isStringFitInFormat(
                        '19.01~w1', RightDate.WEEKDAY_NEAREST_DATE))
        self.assertFalse(RightDate.isStringFitInFormat(
                        'aaa', RightDate.WEEKDAY_AFTER_DATE))
        self.assertFalse(RightDate.isStringFitInFormat(
                        'aaa', RightDate.DATE))
        self.assertFalse(RightDate.isStringFitInFormat(
                        'aaa', RightDate.EASTER))
        self.assertTrue(RightDate.isStringFitInFormat(
                        'w1', RightDate.WEEKDAY))
        self.assertFalse(RightDate.isStringFitInFormat(
                        '19.01-11*w1', RightDate.WEEKDAY))

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestRightDate)
unittest.TextTestRunner(verbosity=2).run(suite)
