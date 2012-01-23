# -*- coding: utf-8 -*-

import Easter
import CalendarReader
import ConsoleVisualizer
import RightDate
import datetime
import StringIO
import unittest

class suite(unittest.TestCase):
    
    def setUp(self):
        self.xml = """<?xml version='1.0' encoding='utf-8'?>
<days>
    <day>
        <date>01.01</date>
        <text>ААА</text>
    </day>
    <day>
        <date>14.04</date>
        <text>ААА</text>
    </day>
    <day>
        <date>E-1</date>
        <text>БББ</text>
    </day>
</days>"""
        self.config = "[Calendar]\ncalendars = c1.xml,c2.xml"
        self.CV = ConsoleVisualizer.ConsoleVisualizer()
    
    def testOldToNewStyle(self):
        self.assertEqual(Easter.oldToNewStyle(datetime.date(2011,  12,  24)),  datetime.date(2012,  1,  6))

    def testNewToOldStyle(self):
        self.assertEqual(Easter.newToOldStyle(datetime.date(2012,  1,  6)),  datetime.date(2011,  12,  24))

    def testEasterDate(self):
        self.assertEqual(Easter.getEasterDate(2001),  datetime.date(2001,  4,  15))
        self.assertEqual(Easter.getEasterDate(2002),  datetime.date(2002,  5,  5))
        self.assertEqual(Easter.getEasterDate(2003),  datetime.date(2003,  4,  27))
        self.assertEqual(Easter.getEasterDate(2004),  datetime.date(2004,  4,  11))
        self.assertEqual(Easter.getEasterDate(2005),  datetime.date(2005,  5,  1))
        self.assertEqual(Easter.getEasterDate(2006),  datetime.date(2006,  4,  23))
        self.assertEqual(Easter.getEasterDate(2007),  datetime.date(2007,  4,  8))
        self.assertEqual(Easter.getEasterDate(2008),  datetime.date(2008,  4,  27))
        self.assertEqual(Easter.getEasterDate(2009),  datetime.date(2009,  4,  19))
        self.assertEqual(Easter.getEasterDate(2010),  datetime.date(2010,  4,  4))
        self.assertEqual(Easter.getEasterDate(2011),  datetime.date(2011,  4,  24))
        self.assertEqual(Easter.getEasterDate(2012),  datetime.date(2012,  4,  15))
        self.assertEqual(Easter.getEasterDate(2013),  datetime.date(2013,  5,  5))
        self.assertEqual(Easter.getEasterDate(2014),  datetime.date(2014,  4,  20))
        self.assertEqual(Easter.getEasterDate(2015),  datetime.date(2015,  4,  12))
        self.assertEqual(Easter.getEasterDate(2016),  datetime.date(2016,  5,  1))
        self.assertEqual(Easter.getEasterDate(2017),  datetime.date(2017,  4,  16))
        self.assertEqual(Easter.getEasterDate(2018),  datetime.date(2018,  4,  8))
        self.assertEqual(Easter.getEasterDate(2019),  datetime.date(2019,  4,  28))
        self.assertEqual(Easter.getEasterDate(2020),  datetime.date(2020,  4,  19))
    
    def testDateToReadableStr(self):
        self.assertEqual(Easter.dateToReadableStr(datetime.date(2020,  4,  19)),  "19 апреля 2020")
        self.assertEqual(Easter.dateToReadableStr(datetime.date(2020,  1,  19)),  "19 января 2020")
    
    def testDateToStr(self):
        self.assertEqual(Easter.dateToStr(datetime.date(2020,  4,  19)),  "19.04")
        self.assertEqual(Easter.dateToStr(datetime.date(2020,  1,  19)),  "19.01")

    def testEasterDistance(self):
        self.assertEqual(Easter.getEasterDistance(datetime.date(2020,  4,  19)), 'E0')
        self.assertEqual(Easter.getEasterDistance(datetime.date(2020,  4,  20)), 'E1')
        self.assertEqual(Easter.getEasterDistance(datetime.date(2020,  4,  18)), 'E-1')
    
    def testParseCalendar(self):
        self.CV.clear()
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml), RightDate.RightDate(datetime.date(2012, 1, 1)),  self.CV, open = lambda s, t: s)
        self.assertEqual(self.CV.__str__(),  "ААА\n".decode('utf-8'))
        self.CV.clear()
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml), RightDate.RightDate(datetime.date(2012,  4,  14)), self.CV, open = lambda s, t: s)
        self.assertEqual(self.CV.__str__(), "ААА\nБББ\n".decode('utf-8'))
        self.assertRaises(CalendarReader.CalendarFileError, lambda : CalendarReader.parseCalendar('calendar1.xml', RightDate.RightDate(datetime.date(2012,  4,  14)), self.CV))
        
    def testLoadCalendars(self):
        self.assertEqual(CalendarReader.getCalendarFilenames(StringIO.StringIO(self.config),  open = lambda s, t: s), ['c1.xml', 'c2.xml'])
        
    def testConsoleVisualizer(self):
        self.CV.clear()
        self.assertEqual(self.CV.__str__(), "")
        self.CV.add("ААА")
        self.CV.add("БББ")
        self.assertEqual(self.CV.__str__(), "ААА\nБББ\n")
    
    def testRightDate(self):
        d = RightDate.RightDate(datetime.date(2012, 1, 1))
        self.assertTrue(d.isRightDate('01.01'))
        d = RightDate.RightDate(datetime.date(2012,  4,  15))
        self.assertTrue(d.isRightDate('E0'))
#        d = RightDate.RightDate(datetime.date(2012,  1,  21))
#        self.assertTrue(d.isRightDate('19.01+1*w6'))
        
    def testIsDate(self):
        self.assertTrue(Easter.isDate('19.01'))
        self.assertTrue(Easter.isDate('E0'))
        self.assertTrue(Easter.isDate('E-154'))
        self.assertFalse(Easter.isDate('19.01+1*w6'))
    
if __name__ == "__main__":
    unittest.main()
    
