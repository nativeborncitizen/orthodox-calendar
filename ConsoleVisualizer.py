# -*- coding: utf-8 -*-

import Visualizer

class ConsoleVisualizer(Visualizer.Visualizer):
    """
    Класс для отображения информации в консоли
    """
        
    def __str__(self):
        """
        Формирование строки для вывода, отсортированной по возрастанию веса
        """
        from operator import itemgetter
        return '\n'.join(map(itemgetter(0),  sorted(self._s, key = lambda t: t[1])))
