# -*- coding: utf-8 -*-
"""
Тесты модуля работы с датами
"""

import datetime
import unittest

from church_calendar import easter


class TestEaster(unittest.TestCase):

    def test_old_to_new_style(self):
        """Тест перевода из старого стиля в новый"""
        self.assertEqual(easter.oldToNewStyle(
                datetime.date(2011, 12, 24)),
                datetime.date(2012, 1, 6))

    def test_new_to_old_style(self):
        """Тест перевода из нового стиля в старый"""
        self.assertEqual(easter.newToOldStyle(
                datetime.date(2012, 1, 6)),
                datetime.date(2011, 12, 24))

    def test_Easter_date(self):
        """Тест определения даты Пасхи"""
        self.assertEqual(easter.get_Easter_date(2001),
                          datetime.date(2001, 4, 15))
        self.assertEqual(easter.get_Easter_date(2002),
                          datetime.date(2002, 5, 5))
        self.assertEqual(easter.get_Easter_date(2003),
                          datetime.date(2003, 4, 27))
        self.assertEqual(easter.get_Easter_date(2004),
                          datetime.date(2004, 4, 11))
        self.assertEqual(easter.get_Easter_date(2005),
                          datetime.date(2005, 5, 1))
        self.assertEqual(easter.get_Easter_date(2006),
                          datetime.date(2006, 4, 23))
        self.assertEqual(easter.get_Easter_date(2007),
                          datetime.date(2007, 4, 8))
        self.assertEqual(easter.get_Easter_date(2008),
                          datetime.date(2008, 4, 27))
        self.assertEqual(easter.get_Easter_date(2009),
                          datetime.date(2009, 4, 19))
        self.assertEqual(easter.get_Easter_date(2010),
                          datetime.date(2010, 4, 4))
        self.assertEqual(easter.get_Easter_date(2011),
                          datetime.date(2011, 4, 24))
        self.assertEqual(easter.get_Easter_date(2012),
                          datetime.date(2012, 4, 15))
        self.assertEqual(easter.get_Easter_date(2013),
                          datetime.date(2013, 5, 5))
        self.assertEqual(easter.get_Easter_date(2014),
                          datetime.date(2014, 4, 20))
        self.assertEqual(easter.get_Easter_date(2015),
                          datetime.date(2015, 4, 12))
        self.assertEqual(easter.get_Easter_date(2016),
                          datetime.date(2016, 5, 1))
        self.assertEqual(easter.get_Easter_date(2017),
                          datetime.date(2017, 4, 16))
        self.assertEqual(easter.get_Easter_date(2018),
                          datetime.date(2018, 4, 8))
        self.assertEqual(easter.get_Easter_date(2019),
                          datetime.date(2019, 4, 28))
        self.assertEqual(easter.get_Easter_date(2020),
                          datetime.date(2020, 4, 19))

    def test_date_to_readable_str(self):
        """Тест конвертации строки в читабельный формат"""
        self.assertEqual(easter.dateToReadableStr(
                datetime.date(2020, 4, 19)), u"19 апреля 2020")
        self.assertEqual(easter.dateToReadableStr(
                datetime.date(2020, 1, 19)), u"19 января 2020")

    def test_date_to_str(self):
        """Тест конвертации даты в строку вида дд.мм"""
        self.assertEqual(easter.dateToStr(
                            datetime.date(2020, 4, 19)), "19.04")
        self.assertEqual(easter.dateToStr(
                            datetime.date(2020, 1, 19)), "19.01")

    def test_str_to_date(self):
        """Тест получения даты из строки вида дд.мм и года"""
        self.assertEqual(easter.strToDate("19.04", 2020),
                            datetime.date(2020, 4, 19))
        self.assertEqual(easter.strToDate("19.01", 2020),
                            datetime.date(2020, 1, 19))

    def test_Easter_distance_from_date(self):
        """Тест определения количества дней до Пасхи"""
        self.assertEqual(easter.getEasterDistanceFromDate(
                                datetime.date(2020, 4, 19)), 'E0')
        self.assertEqual(easter.getEasterDistanceFromDate(
                                datetime.date(2020, 4, 20)), 'E1')
        self.assertEqual(easter.getEasterDistanceFromDate(
                                datetime.date(2020, 4, 18)), 'E-1')

    def test_date_from_Easter_distance(self):
        """Тест получения даты на основании количества дней до Пасхи"""
        self.assertEqual(easter.getDateFromEasterDistance(
                        'E0', 2020), datetime.date(2020, 4, 19))
        self.assertEqual(easter.getDateFromEasterDistance(
                        'E1', 2020), datetime.date(2020, 4, 20))
        self.assertEqual(easter.getDateFromEasterDistance(
                        'E-1', 2020), datetime.date(2020, 4, 18))

    def test_get_weekday_from_date(self):
        """Тест определения n-ого дня недели до/после даты"""
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 1), 1, 6, 1),
                        datetime.date(2012, 1, 7))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 14), 1, 7, 1),
                        datetime.date(2012, 1, 15))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 19), 1, 6, 1),
                        datetime.date(2012, 1, 21))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 4, 5, 1),
                        datetime.date(2012, 3, 9))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 1, 7, 1),
                        datetime.date(2012, 2, 19))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2013, 1, 19), 1, 6, 1),
                        datetime.date(2013, 1, 26))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 1), 1, 6, -1),
                        datetime.date(2011, 12, 31))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 19), 1, 6, -1),
                        datetime.date(2012, 1, 14))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 1, 10), 1, 2, -1),
                        datetime.date(2012, 1, 3))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 4, 5, -1),
                        datetime.date(2012, 1, 20))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2012, 2, 15), 1, 0, -1),
                        datetime.date(2012, 2, 12))
        self.assertEqual(easter.getWeekdayFromDate(
                        datetime.date(2013, 1, 19), 1, 6, -1),
                        datetime.date(2013, 1, 12))

    def test_get_weekday_str(self):
        """Тест определения дня недели в читабельном формате"""
        self.assertEqual(easter.getWeekdayStr(
                    datetime.date(2012, 1, 1)), u'Воскресенье')
        self.assertEqual(easter.getWeekdayStr(
                    datetime.date(2012, 1, 2)), u'Понедельник')
        self.assertEqual(easter.getWeekdayStr(
                    datetime.date(2012, 1, 3)), u'Вторник')
        self.assertEqual(easter.getWeekdayStr(
                    datetime.date(2012, 1, 4)), u'Среда')
        self.assertEqual(easter.getWeekdayStr(
                    datetime.date(2012, 1, 5)), u'Четверг')
        self.assertEqual(easter.getWeekdayStr(
                    datetime.date(2012, 1, 6)), u'Пятница')
        self.assertEqual(easter.getWeekdayStr(
                    datetime.date(2012, 1, 7)), u'Суббота')

    def test_get_weekday_after_dist(self):
        """Тест определения количества дней между днями недели вперед"""
        self.assertEqual(easter.getWeekdayAfterDist(3, 6), 3)
        self.assertEqual(easter.getWeekdayAfterDist(3, 1), 5)

    def test_get_weekday_before_dist(self):
        """Тест определения количества дней между днями недели назад"""
        self.assertEqual(easter.getWeekdayBeforeDist(3, 6), 4)
        self.assertEqual(easter.getWeekdayBeforeDist(3, 1), 2)

    def test_get_nearest_weekday(self):
        """Тест определения ближайшего дня недели"""
        self.assertEqual(easter.getNearestWeekday(
                    datetime.date(2012, 1, 19), 6),
                    datetime.date(2012, 1, 21))
        self.assertEqual(easter.getNearestWeekday(
                    datetime.date(2013, 1, 19), 6),
                    datetime.date(2013, 1, 19))

    def test_shift_date_on_year(self):
        """Тест сдвига даты на год"""
        self.assertEqual(easter.shiftDateOnYear(
                datetime.date(2012, 1, 20), 1),
                datetime.date(2013, 1, 20))
        self.assertEqual(easter.shiftDateOnYear(
                datetime.date(2012, 1, 20), -1),
                datetime.date(2011, 1, 20))
        self.assertRaises(ValueError, lambda:
            easter.shiftDateOnYear(
                        datetime.date(2012, 2, 29), 1))
        
    def test_get_voice(self):
        """Тест определения гласа"""
        self.assertEqual(easter.get_voice(datetime.date(2012, 4, 21)), None)
        self.assertEqual(easter.get_voice(datetime.date(2012, 4, 15)), None)
        self.assertEqual(easter.get_voice(datetime.date(2012, 4, 22)), 1)
        self.assertEqual(easter.get_voice(datetime.date(2012, 6, 2)), 6)
        self.assertEqual(easter.get_voice(datetime.date(2012, 6, 3)), 7)
        self.assertEqual(easter.get_voice(datetime.date(2012, 5, 17)), 4)
        self.assertEqual(easter.get_voice(datetime.date(2012, 3, 16)), 6)
        self.assertEqual(easter.get_voice(datetime.date(2012, 4, 7)), 1)
        self.assertEqual(easter.get_voice(datetime.date(2012, 6, 10)), 8)
        self.assertEqual(easter.get_voice(datetime.date(2013, 4, 21)), 5)
        self.assertEqual(easter.get_voice(datetime.date(2012, 4, 8)), None)
        
    def test_get_week_after_Easter(self):
        '''Тест определения номера недели после Пасхи'''
        self.assertEqual(easter.get_week_after_Easter(
                datetime.date(2012, 4, 22)), 2)
        self.assertEqual(easter.get_week_after_Easter(
                datetime.date(2012, 4, 28)), 2)
        self.assertEqual(easter.get_week_after_Easter(
                datetime.date(2012, 4, 29)), 3)
        self.assertEqual(easter.get_week_after_Easter(
                datetime.date(2012, 2, 1)), 41)
        

suite = unittest.TestLoader().loadTestsFromTestCase(
                                                TestEaster)
unittest.TextTestRunner(verbosity=2).run(suite)
