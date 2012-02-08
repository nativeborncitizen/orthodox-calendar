# -*- coding: utf-8 -*-


class ConsoleVisualizer:
    """
    Класс для отображения информации в консоли
    """
    def __init__(self):
        self._s = []

    def add(self, text,  score):
        """
        Добавление новой строки
        вход: строка
        вход: вес для сортировки
        """
        self._s.append((text,  score))

    def clear(self):
        """
        Очистить содержимое буфера
        """
        self._s = []

    def __str__(self):
        """
        Формирование строки для вывода,
        отсортированной по возрастанию веса
        """
        from operator import itemgetter
        return '\n'.join(map(itemgetter(0),
                             sorted(self._s, key = lambda t: t[1])))
