# -*- coding: utf-8 -*-

import Easter
import datetime
import re

DATE_OR_EASTER = re.compile('\d\d\.\d\d$|E-?\d+$') # дд.мм или E[-]n
WEEKDAY_AFTER_DATE = re.compile('\d\d\.\d\d[+-]\d+\*w\d$')

def isStringFitInFormat(s,  format):
    """
    Проверка текста на соответствие формату
    вход: строка, формат
    выход: True/False
    """
    return format.match(s) is not None

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
        if isStringFitInFormat(xmlDate, DATE_OR_EASTER):
            return xmlDate in self.dateList
        elif sStringFitInFormat(xmlDate, WEEKDAY_AFTER_DATE):
            return True
        else:
            return False
