# -*- coding: utf-8 -*-

import Easter
import datetime
import re

DATE_OR_EASTER = re.compile('\d\d\.\d\d$|E-?\d+$') # дд.мм или E[-]n
WEEKDAY_AFTER_DATE = re.compile('\d\d\.\d\d[-+]\d\d\*w[1-7]') # шаблон для случаев вида "первая суббота по Богоявлении"

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
        self.date = date
        self.dateList = [Easter.dateToStr(date),  Easter.getEasterDistance(date)]
    
    def isRightDate(self,  xmlDate):
        """
        Проверка, соответствует ли выбранная дата той, которая найдена в XML-файле
        вход: дата из XML-файла
       """
        if isStringFitInFormat(xmlDate, DATE_OR_EASTER):
            return xmlDate in self.dateList
        elif isStringFitInFormat(xmlDate, WEEKDAY_AFTER_DATE):
            d, m = xmlDate[0 : 5].split('.')
            n = xmlDate[6 : 8]
            w = xmlDate[-1]
            if xmlDate[5] == '+':
                return self.date == Easter.getWeekdayAfterDate(int(d), int(m), self.date.year, int(n), int(w))
            else:
                return self.date == Easter.getWeekdayBeforeDate(int(d), int(m), self.date.year, int(n), int(w))
        else:
            return False
