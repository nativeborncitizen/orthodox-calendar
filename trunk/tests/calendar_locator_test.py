# -*- coding: utf-8 -*-
"""
Тесты модуля поиска файлов-календарей в указанном каталоге
"""


import unittest
import StringIO

from church_calendar import calendar_locator


class TestCalendarLocator(unittest.TestCase):

    def setUp(self):
        self.config = "[Calendar]\ncalendars = c1.xml,c2.xml"

    def testLoadCalendars(self):
        self.assertEqual(
            calendar_locator.get_calendar_filenames_from_config(
            StringIO.StringIO(self.config),
            open_ = lambda s, t: s), ['c1.xml', 'c2.xml'])

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestCalendarLocator)
unittest.TextTestRunner(verbosity=2).run(suite)
