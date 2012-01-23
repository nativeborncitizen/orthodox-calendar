# -*- coding: utf-8 -*-

import Easter
import datetime

class RightDate:
    """
    Класс для опеределения соответствия текущей даты дате из XML-файла
    """
    def __init__(self, date):
        """
        Конструктор
        вход: дата, для которой нужно получить календарь
        """
        self.dateList = [Easter.dateToStr(date),  Easter.getEasterDistance(date)]
        
    def isRightDate(self,  xmlDate):
        """
        Проверка, соответствует ли выбранная дата той, которая найдена в XML-файле
        вход: дата из XML-файла
        """
        return xmlDate in self.dateList
