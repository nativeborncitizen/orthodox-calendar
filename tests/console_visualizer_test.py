# -*- coding: utf-8 -*-
"""
Модуль для тестирования отображения атрибутов дня в консоли
"""
import StringIO
import unittest
import console_visualizer
import fasts_and_feasts


class  ConsoleVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.DD = type("Mock", (object, ), {
                "get_texts": lambda self: [
                        (u"ААА", 1000),
                        (u"БББ", 1000),
                ],
                "get_fast": lambda self: u"ВВВ",
                "get_date": lambda self: u"А",
                "get_old_style_date": lambda self: u"Б",
                "get_weekday": lambda self: u"Д",
        })()
    
    def test_console_visualizer_(self):
        """Тест рендера в консоль"""
        buf = StringIO.StringIO()
        console_visualizer.render(self.DD, file_=buf)
        self.assertEqual(buf.getvalue(),
                "Д, А\n(Б ст. ст.)\nВВВ\nААА\nБББ")

    def test_render_texts(self):
        """Тест рендера праздников"""
        self.assertEqual(console_visualizer.render_texts([
                (u"ААА", 1000),
                (u"ВВВ", fasts_and_feasts.TIPIKON_SIGNS.FULL_CROSS),
                ]),
                u"ААА\n(+) ВВВ")


suite = unittest.TestLoader().loadTestsFromTestCase(
                                                ConsoleVisualizerTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)

