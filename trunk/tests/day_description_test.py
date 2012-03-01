# -*- coding: utf-8 -*-
"""
Тест для модуля, который собирает все атрибуты дня
"""
import unittest
import day_description


class  DayDescriptionTestCase(unittest.TestCase):
    """
    Тестирование сбора атрибутов
    """
    def setUp(self):
        self.DD = day_description.DayDescription()

    def test_day_description(self):
        """Тест контейнера для описания всех атрибутов дня"""
        self.DD.add_text("ААА",  1)
        self.DD.add_text("БББ",  0)
        self.assertEqual(self.DD.get_text(), ["БББ","ААА"])
        self.DD.add_fast("mm",  1)
        self.DD.add_fast("np",  3)
        self.assertEqual(
            self.DD.get_fast(), u"Нет поста")

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                DayDescriptionTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)

