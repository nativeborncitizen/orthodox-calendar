# -*- coding: utf-8 -*-
"""
Тесты модуля разбора файлов календаря
"""

import unittest
import StringIO
import CalendarReader


class TestCalendarReader(unittest.TestCase):

    def setUp(self):
        self.xml = """<?xml version='1.0' encoding='utf-8'?>
<days>
    <day date = '01.01'>
        <text tipikon = '1000'>АА1</text>
        <text score = '0'>АА2</text>
        <text tipikon = '100' score = '12'>АА3</text>
        <fast type='st' priority = '1'/>
        <fast type='ol' polyeley='True' priority = '1'/>
    </day>
</days>"""

        def add_text(self, s, i, t):
            self.text.append((s, i, t))

        def add_fast(self, s, i, p=False):
            self.fast.append((s, i, p))

        self.DD = type("Mock", (object, ), {
                "text": [],
                "fast": [],
                "add_text": add_text,
                "add_fast": add_fast,
                "MAX_SCORE": 1000
                }) ()

        self.DT = type("Mock", (object, ), {
                "isRightDate": lambda self, d: True
        }) ()

    def testParseCalendar(self):
        """Тест разбора xml-файла"""
        CalendarReader.parseCalendar(StringIO.StringIO(self.xml), 
                self.DT, self.DD, open = lambda s, t: s)
        self.assertEqual(self.DD.text, [
                (u"АА1", 1000, '1000'),
                (u"АА2", 0, ''),
                (u"АА3", 12, '100')
        ])
        self.assertEqual(self.DD.fast, [
                ("st", '1', False),
                ("ol", '1', True)
        ])


suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestCalendarReader)
unittest.TextTestRunner(verbosity=2).run(suite)
