# -*- coding: utf-8 -*-

import datetime
import StringIO
import unittest

import Easter
import CalendarReader
import ConsoleVisualizer
import RightDate
import CalendarLocator

class suite(unittest.TestCase):

    def setUp(self):
        self.xml = """<?xml version='1.0' encoding='utf-8'?>
<days>
    <day date = '01.01'>
        <text>АА1</text>
        <text score = '0'>АА2</text>
        <text score = '12'>АА3</text>
    </day>
    <day date = '14.04'>
        <text>ААА</text>
    </day>
    <day date = 'E-1'>
        <text>БББ</text>
    </day>
    <day date = 'E-5:E-4'>
        <text>ВВВ</text>
    </day>
</days>"""
        self.config = "[Calendar]\ncalendars = c1.xml,c2.xml"
        self.CV = ConsoleVisualizer.ConsoleVisualizer()

    def testOldToNewStyle(self):
        self.assertEqual(Easter.oldToNewStyle(datetime.date(2011,
                            12, 24)),  datetime.date(2012,  1,  6))

    def testNewToOldStyle(self):
        self.assertEqual(Easter.newToOldStyle(datetime.date(2012,
                            1,  6)),  datetime.date(2011,  12,  24))

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
        self.assertEqual(Easter.dateToReadableStr(
                datetime.date(2020,  4,  19)),  "19 апреля 2020")
        self.assertEqual(Easter.dateToReadableStr(
                datetime.date(2020,  1,  19)),  "19 января 2020")

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

    def testParseCalendar(self):
        self.CV.clear()
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml),
                    RightDate.RightDate(datetime.date(2012, 1, 1)),
                    self.CV, open = lambda s, t: s)
        self.assertEqual(self.CV.__str__(),
                    "АА2\nАА3\nАА1".decode('utf-8'))
        self.CV.clear()
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml),
                    RightDate.RightDate(datetime.date(2012, 4, 14)),
                    self.CV, open = lambda s, t: s)
        self.assertEqual(self.CV.__str__(),
                    "ААА\nБББ".decode('utf-8'))
        self.CV.clear()
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml),
                    RightDate.RightDate(datetime.date(2012, 4, 11)),
                    self.CV, open = lambda s, t: s)
        self.assertEqual(self.CV.__str__(), "ВВВ".decode('utf-8'))
        self.assertRaises(CalendarReader.CalendarFileError,
                    lambda : CalendarReader.parseCalendar(
                    'calendar1.xml', RightDate.RightDate(
                    datetime.date(2012,  4,  14)), self.CV))

    def testLoadCalendars(self):
        self.assertEqual(
                CalendarLocator.getCalendarFilenamesFromConfig(
                StringIO.StringIO(self.config),
                open = lambda s, t: s), ['c1.xml', 'c2.xml'])

    def testConsoleVisualizer(self):
        self.CV.clear()
        self.assertEqual(self.CV.__str__(), "")
        self.CV.add("ААА",  1)
        self.CV.add("БББ",  0)
        self.assertEqual(self.CV.__str__(), "БББ\nААА")

    def testRightDate(self):
        d = RightDate.RightDate(datetime.date(2012, 1, 1))
        self.assertEqual(d.isRightDate('01.01'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 4, 15))
        self.assertEqual(d.isRightDate('E0'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 1, 21))
        self.assertEqual(d.isRightDate('19.01+01*w6'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 1, 11))
        self.assertEqual(d.isRightDate('19.01-02*w3'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 1, 11))
        self.assertEqual(d.isRightDate('10.01:20.01'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 4, 14))
        self.assertEqual(d.isRightDate('13.04:E0'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 4, 13))
        self.assertEqual(d.isRightDate('13.04:E0'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 4, 12))
        self.assertEqual(d.isRightDate('13.04:E0'), (False, 1))
        d = RightDate.RightDate(datetime.date(2012, 4, 12))
        self.assertEqual(d.isRightDate('13.04:aq'), (False, 1))
        d = RightDate.RightDate(datetime.date(2012, 1, 21))
        self.assertEqual(d.isRightDate('19.01~w6'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 2, 8))
        self.assertEqual(d.isRightDate('w3'), (True, 1))
        d = RightDate.RightDate(datetime.date(2012, 2, 8))
        self.assertEqual(d.isRightDate('w3&01.02:10.02&08.02'),
                            (True, 3))

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
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 1)), 'Воскресенье')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 2)), 'Понедельник')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 3)), 'Вторник')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 4)), 'Среда')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 5)), 'Четверг')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 6)), 'Пятница')
        self.assertEqual(Easter.getWeekdayStr(
                    datetime.date(2012, 1, 7)), 'Суббота')

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

if __name__ == "__main__":
    unittest.main()
