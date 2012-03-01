# -*- coding: utf-8 -*-
"""
Модуль для тестирования отображения атрибутов дня в консоли
"""
import StringIO
import unittest
import console_visualizer


class  ConsoleVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.DD = type("Mock", (object, ), {
                "get_text": lambda self: [u"ААА", u"БББ"],
                "get_fast": lambda self: u"ВВВ"})()
    
    def test_console_visualizer_(self):
        """Тест рендера в консоль"""
        buffer = StringIO.StringIO()
        console_visualizer.render(self.DD, file_=buffer)
        self.assertEqual(buffer.getvalue(),
                "ВВВ\nААА\nБББ")


suite = unittest.TestLoader().loadTestsFromTestCase(
                                                ConsoleVisualizerTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)

