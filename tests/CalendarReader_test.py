# -*- coding: utf-8 -*-
"""
Тесты модуля разбора файлов календаря
"""

import unittest
import StringIO
import datetime
import CalendarReader
import RightDate


class TestCalendarReader(unittest.TestCase):

    def setUp(self):
        self.xml = """<?xml version='1.0' encoding='utf-8'?>
<days>
    <day date = '01.01'>
        <text>АА1</text>
        <text score = '0'>АА2</text>
        <text score = '12'>АА3</text>
        <fast type='st' priority = '1'/>
    </day>
</days>"""

        def add_text(self, s, i):
            self.text.append((s, i))

        def add_fast(self, s, i):
            self.fast.append((s, i))

        self.DD = type("Mock", (object, ), {
                "text": [],
                "fast": [],
                "add_text": add_text,
                "add_fast": add_fast
                }) ()

    def testParseCalendar(self):
        """Тест разбора xml-файла"""
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml),
                    RightDate.RightDate(datetime.date(2012, 1, 1)),
                    self.DD, open = lambda s, t: s)
        self.assertEqual(self.DD.text, [
                (u"АА1", 1000),
                (u"АА2", 0),
                (u"АА3", 12),
        ])
        self.assertEqual(self.DD.fast, [
                ("st", '1')
        ])


suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestCalendarReader)
unittest.TextTestRunner(verbosity=2).run(suite)
