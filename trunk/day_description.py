# -*- coding: utf-8 -*-
"""
Модуль-контейнер для хранения всех атрибутов дня
"""
from operator import itemgetter

import fasts_and_hollidays


__author__="z"
__date__ ="$1 бер 2012 0:40:17$"

class DayDescription(object):
    """
    Класс-контейнер для хранения информации об атрибутах дня
    """
    def __init__(self):
        """
        Инициализация контейнера (без параметров)
        """
        self._text = []
        self._fast = ('', 0)

    def add_text(self, text,  score):
        """
        Добавление новой строки с описанием праздника
        вход: строка
        вход: вес для сортировки
       """
        self._text.append((text,  score))

    def get_text(self):
        """
        Вернуть все строки описаний праздников, отсортированые по score
        """
        return map(itemgetter(0),
                sorted(self._text, key = lambda t: t[1]))

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
