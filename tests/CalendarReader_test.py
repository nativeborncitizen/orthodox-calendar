# -*- coding: utf-8 -*-
"""
Тесты модуля разбора файлов календаря
"""


import unittest
import StringIO
import datetime

import CalendarReader
import ConsoleVisualizer
import RightDate

class TestCalendarReader(unittest.TestCase):

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
    <day date = 'E-5:E-3'>
        <text>ВВВ</text>
    </day>
    <day date = '03.05'>
        <text>ААА</text>
        <fast type='mm'/>
    </day>
    <day date = 'E-7:E-1@03.05'>
        <text>ВВВ</text>
        <fast type='st' priority = '1'/>
    </day>
</days>"""

        self.CV = ConsoleVisualizer.ConsoleVisualizer()

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
        self.CV.clear()
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml),
                    RightDate.RightDate(datetime.date(2002, 5, 3)),
                    self.CV, open = lambda s, t: s)
        self.assertEqual(self.CV.__str__(),
                    "Строгий пост\nААА\nВВВ".decode('utf-8'))

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestCalendarReader)
unittest.TextTestRunner(verbosity=2).run(suite)
