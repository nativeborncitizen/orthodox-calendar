# -*- coding: utf-8 -*-

import Visualizer

class ConsoleVisualizer(Visualizer.Visualizer):
    """
    Класс для отображения информации в консоли
    """
    def add(self, s):
        self._s += "%s\n" % s
