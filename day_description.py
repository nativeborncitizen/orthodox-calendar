# -*- coding: utf-8 -*-
"""
Модуль-контейнер для хранения всех атрибутов дня
"""
import fasts_and_hollidays


__author__="nativeborncitizen@blogspot.com"
__date__ ="$1 бер 2012 0:40:17$"

class DayDescription(object):
    """
    Класс-контейнер для хранения информации об атрибутах дня
    """
    MAX_SCORE = 1000 # Вес праздника по умолчанию
    
    def __init__(self):
        """
        Инициализация контейнера (без параметров)
        """
        self._texts = []
        self._fast = ('', 0)

    def add_text(self, text,  score,
            tipikon_sign=""):
        """
        Добавление новой строки с описанием праздника
        вход: строка
        вход: вес для сортировки
        вход: знак типикона (по умолчанию, без знака)
        """
        self._texts.append((text,  score,
                fasts_and_hollidays.get_holliday_type(tipikon_sign)))

    def get_texts(self):
        """
        Вернуть список строк описаний праздников, отсортированный по score
        """
        return [(text[0], text[2]) for text in
                sorted(self._texts, key = lambda t: t[1])]

    def add_fast(self, fast, priority):
        """
        Добавление информации о посте
        вход: код поста
        вход: приоритет поста (сохраняется пост с наибольшим
                приоритетом
       """
        if priority > self._fast[1]:
           self._fast = (fast, priority)

    def get_fast(self):
        """
        Вернуть описание поста
        """
        return fasts_and_hollidays.get_fast_name(self._fast[0])


if __name__ == "__main__":
    pass
