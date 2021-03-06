# -*- coding: utf-8 -*-
"""
Тесты модуля описания постов
"""


import unittest

from church_calendar import fasts_and_feasts

class TestFasts(unittest.TestCase):

    def test_get_fast_name(self):
        """Тест получения описания поста"""
        self.assertEqual(fasts_and_feasts.get_fast_name('st'),
                'Строгий пост'.decode('utf-8'))

    def test_get_holliday_type(self):
        """Тест определения типа праздника"""
        self.assertEqual(fasts_and_feasts.get_holliday_type("FC"),
                fasts_and_feasts.TIPIKON_SIGNS.FULL_CROSS)
        self.assertEqual(fasts_and_feasts.get_holliday_type("qqq"),
                fasts_and_feasts.TIPIKON_SIGNS.WITHOUT)



suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestFasts)
unittest.TextTestRunner(verbosity=2).run(suite)
