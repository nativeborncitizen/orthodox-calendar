# -*- coding: utf-8 -*-
"""
Тесты модуля отображения календаря
"""


import unittest

import ConsoleVisualizer

class TestConsoleVisualizer(unittest.TestCase):

    def setUp(self):
        self.CV = ConsoleVisualizer.ConsoleVisualizer()

    def testConsoleVisualizer(self):
        self.CV.clear()
        self.assertEqual(self.CV.__str__(), "")
        self.CV.addText("ААА",  1)
        self.CV.addText("БББ",  0)
        self.assertEqual(self.CV.__str__(), "БББ\nААА")
        self.CV.clear()
        self.CV.addText("ААА".decode('utf-8'),  1)
        self.CV.addFast("mm",  1)
        self.CV.addFast("np",  3)
        self.assertEqual(
            self.CV.__str__(), "ААА\nНет поста".decode('utf-8'))

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestConsoleVisualizer)
unittest.TextTestRunner(verbosity=2).run(suite)
