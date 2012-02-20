# -*- coding: utf-8 -*-
"""
Тесты модуля поиска файлов-календарей в указанном каталоге
"""


import unittest
import StringIO

import CalendarLocator


class TestCalendarLocator(unittest.TestCase):

    def setUp(self):
        self.config = "[Calendar]\ncalendars = c1.xml,c2.xml"

    def testLoadCalendars(self):
        self.assertEqual(
            CalendarLocator.getCalendarFilenamesFromConfig(
            StringIO.StringIO(self.config),
            open = lambda s, t: s), ['c1.xml', 'c2.xml'])

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestCalendarLocator)
unittest.TextTestRunner(verbosity=2).run(suite)
