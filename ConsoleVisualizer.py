# -*- coding: utf-8 -*-

import fasts_and_hollidays

FAST_SCORE = 35

class ConsoleVisualizer:
    """
    Класс для отображения информации в консоли
    """
    def __init__(self):
        self._text = []
        self._fast = ('', 0)

    def addText(self, text,  score):
        """
        Добавление новой строки
        вход: строка
        вход: вес для сортировки
       """
        self._text.append((text,  score))

    def addFast(self, fast, priority):
        """
        Добавление информации о посте
        вход: код поста
        вход: приоритет поста (сохраняется пост с наибольшим
                приоритетом
       """
        if priority > self._fast[1]:
           self._fast = (fast, priority)

    def clear(self):
        """
        Очистить содержимое буфера
        """
        self._text = []
        self._fast = ('', 0)

    def __str__(self):
        """
        Формирование строки для вывода,
        отсортированной по возрастанию веса
        """
        from operator import itemgetter
        tmp = self._text
        if self._fast[0] != '':
            tmp.append(
                    (fasts_and_hollidays.getFastName(self._fast[0]), FAST_SCORE))
        return '\n'.join(map(itemgetter(0),
                        sorted(tmp, key = lambda t: t[1])))
