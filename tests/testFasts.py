# -*- coding: utf-8 -*-
"""
Тесты модуля описания постов
"""


import unittest

import Fasts

class TestFasts(unittest.TestCase):

    def testGetFastName(self):
        self.assertEqual(Fasts.getFastName('st'),
                'Строгий пост'.decode('utf-8'))

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestFasts)
unittest.TextTestRunner(verbosity=2).run(suite)
