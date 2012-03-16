# -*- coding: utf-8 -*-
"""
Тест для модуля, который собирает все атрибуты дня
"""
import unittest
import datetime
import day_description
import fasts_and_feasts



class  DayDescriptionTestCase(unittest.TestCase):
    """
    Тестирование сбора атрибутов
    """
    def setUp(self):
        self.DD = day_description.DayDescription(datetime.date(2012, 3, 8))

    def test_day_description(self):
        """Тест контейнера для описания всех атрибутов дня"""
        self.DD.add_text("ААА",  100)
        self.DD.add_text("БББ",  0)
        self.DD.add_text("ВВВ",  1000, "FC")
        self.assertEqual(self.DD.get_texts(), [
            ("БББ", fasts_and_feasts.TIPIKON_SIGNS.WITHOUT),
            ("ВВВ", fasts_and_feasts.TIPIKON_SIGNS.FULL_CROSS),
            ("ААА", fasts_and_feasts.TIPIKON_SIGNS.WITHOUT)
        ])
        self.DD.add_fast("mm",  1)
        self.DD.add_fast("np",  3)
        self.assertEqual(
            self.DD.get_fast(), u"Нет поста")

    def test_fasts_in_polyeley(self):
        """Тест определения строгости поста в полиелейные праздники"""
        self.DD.add_text("ААА", 1000, "HC")
        self.DD.add_text("ААА", 1000)
        self.DD.add_text("ААА", 1000, "SL")
        self.DD.add_fast("st",  1)
        self.DD.add_fast("ol",  1, self.DD.POLYELEY)
        self.assertEqual(
            self.DD.get_fast(), u"Разрешена пища с раститительным маслом")

    def test_add_and_get_date(self):
        """Тест занесения и получения даты в контейнере дня"""
        self.assertEqual(self.DD.get_date(), u"8 марта 2012")
        self.assertEqual(self.DD.get_old_style_date(), u"24 февраля 2012")
        self.assertEqual(self.DD.get_weekday(), u"Четверг")

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                DayDescriptionTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)

