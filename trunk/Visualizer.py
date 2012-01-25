# -*- coding: utf-8 -*-

class Visualizer:
    """
    Базовый класс для формирования форматированной строки
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
        return self._s
