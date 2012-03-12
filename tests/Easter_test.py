# -*- coding: utf-8 -*-
"""
Тесты модуля работы с датами
"""

import datetime
import unittest

import Easter


class TestEaster(unittest.TestCase):

    def testOldToNewStyle(self):
        self.assertEqual(Easter.oldToNewStyle(
                datetime.date(2011, 12, 24)),
                datetime.date(2012,  1,  6))

    def testNewToOldStyle(self):
        self.assertEqual(Easter.newToOldStyle(
                datetime.date(2012, 1,  6)),
                datetime.date(2011,  12,  24))

    def testEasterDate(self):
        self.assertEqual(Easter.getEasterDate(2001),
                          datetime.date(2001,  4,  15))
        self.assertEqual(Easter.getEasterDate(2002),
                          datetime.date(2002,  5,  5))
        self.assertEqual(Easter.getEasterDate(2003),
                          datetime.date(2003,  4,  27))
        self.assertEqual(Easter.getEasterDate(2004),
                          datetime.date(2004,  4,  11))
        self.assertEqual(Easter.getEasterDate(2005),
                          datetime.date(2005,  5,  1))
        self.assertEqual(Easter.getEasterDate(2006),
                          datetime.date(2006,  4,  23))
        self.assertEqual(Easter.getEasterDate(2007),
                          datetime.date(2007,  4,  8))
        self.assertEqual(Easter.getEasterDate(2008),
                          datetime.date(2008,  4,  27))
        self.assertEqual(Easter.getEasterDate(2009),
                          datetime.date(2009,  4,  19))
        self.assertEqual(Easter.getEasterDate(2010),
                          datetime.date(2010,  4,  4))
        self.assertEqual(Easter.getEasterDate(2011),
                          datetime.date(2011,  4,  24))
        self.assertEqual(Easter.getEasterDate(2012),
                          datetime.date(2012,  4,  15))
        self.assertEqual(Easter.getEasterDate(2013),
                          datetime.date(2013,  5,  5))
        self.assertEqual(Easter.getEasterDate(2014),
                          datetime.date(2014,  4,  20))
        self.assertEqual(Easter.getEasterDate(2015),
                          datetime.date(2015,  4,  12))
        self.assertEqual(Easter.getEasterDate(2016),
                          datetime.date(2016,  5,  1))
        self.assertEqual(Easter.getEasterDate(2017),
                          datetime.date(2017,  4,  16))
        self.assertEqual(Easter.getEasterDate(2018),
                          datetime.date(2018,  4,  8))
        self.assertEqual(Easter.getEasterDate(2019),
                          datetime.date(2019,  4,  28))
        self.assertEqual(Easter.getEasterDate(2020),
                          datetime.date(2020,  4,  19))

    def testDateToReadableStr(self):
        """Тест конвертации строки в читабельный формат"""
        self.assertEqual(Easter.dateToReadableStr(
                datetime.date(2020,  4,  19)),  u"19 апреля 2020")
        self.assertEqual(Easter.dateToReadableStr(
                datetime.date(2020,  1,  19)),  u"19 января 2020")

    def testDateToStr(self):
        self.assertEqual(Easter.dateToStr(
                            datetime.date(2020,  4,  19)),  "19.04")
        self.assertEqual(Easter.dateToStr(
                            datetime.date(2020,  1,  19)),  "19.01")

    def testStrToDate(self):
        self.assertEqual(Easter.strToDate("19.04", 2020),
                            datetime.date(2020,  4,  19))
        self.assertEqual(Easter.strToDate("19.01", 2020),
                            datetime.date(2020,  1,  19))

    def testEasterDistanceFromDate(self):
        self.assertEqual(Easter.getEasterDistanceFromDate(
                                datetime.date(2020,  4,  19)), 'E0')
        self.assertEqual(Easter.getEasterDistanceFromDate(
                                datetime.date(2020,  4,  20)), 'E1')
        self.assertEqual(Easter.getEasterDistanceFromDate(
                                datetime.date(2020,  4,  18)), 'E-1')

    def testDateFromEasterDistance(self):
        self.assertEqual(Easter.getDateFromEasterDistance(
                        'E0', 2020), datetime.date(2020,  4,  19))
        self.assertEqual(Easter.getDateFromEasterDistance(
                        'E1', 2020), datetime.date(2020,  4,  20))
        self.assertEqual(Easter.getDateFromEasterDistance(
                        'E-1', 2020), datetime.date(2020,  4,  18))

    def testGetWeekdayFromDate(self):
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 1), 1, 6, 1),
                        datetime.date(2012, 1, 7))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 14), 1, 7, 1),
                        datetime.date(2012, 1, 15))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 19), 1, 6, 1),
                        datetime.date(2012, 1, 21))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 4, 5, 1),
                        datetime.date(2012, 3, 9))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 1, 7, 1),
                        datetime.date(2012, 2, 19))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2013, 1, 19), 1, 6, 1),
                        datetime.date(2013, 1, 26))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 1), 1, 6, -1),
                        datetime.date(2011, 12, 31))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 19), 1, 6, -1),
                        datetime.date(2012, 1, 14))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 10), 1, 2, -1),
                        datetime.date(2012, 1, 3))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 4, 5, -1),
                        datetime.date(2012, 1, 20))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 1, 0, -1),
                        datetime.date(2012, 2, 12))
        self.assertEqual(Easter.getWeekdayFromDate(
                        datetime.date(2013, 1, 19), 1, 6, -1),
                        datetime.date(2013, 1, 12))

    def testGetWeekdayStr(self):
        """Тест определения дня недели в читабельном формате"""
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 1)), u'Воскресенье')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 2)), u'Понедельник')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 3)), u'Вторник')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 4)), u'Среда')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 5)), u'Четверг')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 6)), u'Пятница')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 7)), u'Суббота')

    def testGetWeekdayAfterDist(self):
        self.assertEqual(Easter.getWeekdayAfterDist(3, 6), 3)
        self.assertEqual(Easter.getWeekdayAfterDist(3, 1), 5)

    def testGetWeekdayDtforeDist(self):
        self.assertEqual(Easter.getWeekdayBeforeDist(3, 6), 4)
        self.assertEqual(Easter.getWeekdayBeforeDist(3, 1), 2)

    def testGetNearestWeekday(self):
        self.assertEqual(Easter.getNearestWeekday(
                    datetime.date(2012, 1, 19), 6),
                    datetime.date(2012, 1, 21))
        self.assertEqual(Easter.getNearestWeekday(
                    datetime.date(2013, 1, 19), 6),
                    datetime.date(2013, 1, 19))

    def testShiftDateOnYear(self):
        self.assertEqual(Easter.shiftDateOnYear(
                datetime.date(2012, 1, 20), 1),
                datetime.date(2013, 1, 20))
        self.assertEqual(Easter.shiftDateOnYear(
                datetime.date(2012, 1, 20), -1),
                datetime.date(2011, 1, 20))
        self.assertRaises(ValueError, lambda:
            Easter.shiftDateOnYear(
                        datetime.date(2012, 2, 29), 1))

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestEaster)
unittest.TextTestRunner(verbosity=2).run(suite)
