# -*- coding: utf-8 -*-

class Visualizer:
    """
    Базовый класс для формирования форматированной строки
    """
    def __init__(self):
        self._s = ""
        
    def add(self,  s):
        """
        Добавить в буфер новую строку с описанием дня
        вход - строка для добавления
        """
        pass
        
    def clear(self):
        """
        Очистить содержимое буфера
        """
        self._s = ""
        
    def __str__(self):
        return self._s
