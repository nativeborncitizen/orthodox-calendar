# -*- coding: utf-8 -*-

import Easter
import CalendarReader
import datetime
import unittest

class suite(unittest.TestCase):
    
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
        self.assertEqual(CalendarReader.parseCalendar('calendar.xml', ['07.01']),  "Рождество Господа и Спаса нашего Иисуса Христа.\n".decode('utf-8'))
        self.assertEqual(CalendarReader.parseCalendar('calendar.xml', ['07.01', 'E0']), "Рождество Господа и Спаса нашего Иисуса Христа.\nСветлое Христово Воскресение. Пасха.\n".decode('utf-8'))
        self.assertRaises(CalendarReader.CalendarFileError, lambda : CalendarReader.parseCalendar('calendar1.xml', ['07.01']))
        
    def testLoadCalendars(self):
        import StringIO
        self.assertEqual(CalendarReader.getCalendarFilenames(StringIO.StringIO("[Calendar]\ncalendars = c1.xml,c2.xml"),  open = lambda s, t: s), ['c1.xml', 'c2.xml'])
    
if __name__ == "__main__":
    unittest.main()
    
