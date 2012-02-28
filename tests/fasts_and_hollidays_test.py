# -*- coding: utf-8 -*-
"""
Тесты модуля описания постов
"""


import unittest

import fasts_and_hollidays

class TestFasts(unittest.TestCase):

    def testGetFastName(self):
        self.assertEqual(fasts_and_hollidays.getFastName('st'),
                'Строгий пост'.decode('utf-8'))

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestFasts)
unittest.TextTestRunner(verbosity=2).run(suite)
