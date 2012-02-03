# -*- coding: utf-8 -*-

import Easter
import datetime
import re

DATE = re.compile('\d\d\.\d\d$') # E[-]n
EASTER = re.compile('E-?\d+$') # E[-]n
WEEKDAY_AFTER_DATE = re.compile('\d\d\.\d\d[-+]\d\d\*w[1-7]') # шаблон для случаев вида "первая суббота по Богоявлении"
WEEKDAY_NEAREST_DATE = re.compile('\d\d\.\d\d~w[1-7]') # шаблон для случаев вида "ближайшее воскресенье к ..."

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
        self.strDate = Easter.dateToStr(date)
        self.distEaster = Easter.getEasterDistanceFromDate(date)
    
    def isRightDate(self,  xmlDate):
        """
        Проверка, соответствует ли выбранная дата той, которая найдена в XML-файле
        вход: дата из XML-файла
        выход: True/False
       """
        if ':' in xmlDate: # интервал
            dates = xmlDate.split(':')
            
            return True
        elif isStringFitInFormat(xmlDate, DATE):
            return xmlDate == self.strDate
        elif isStringFitInFormat(xmlDate, EASTER):
            return xmlDate == self.distEaster
        elif isStringFitInFormat(xmlDate, WEEKDAY_AFTER_DATE):
            d, m = xmlDate[0 : 5].split('.')
            n = xmlDate[6 : 8]
            w = xmlDate[-1]
            date = datetime.date(self.date.year, int(m), int(d))
            if xmlDate[5] == '+':
                s = 1
            else:
                s = -1
            passDate = Easter.dateToStr(Easter.getWeekdayFromDate(date, int(n), int(w), s))
            return self.strDate == passDate
        elif isStringFitInFormat(xmlDate, WEEKDAY_NEAREST_DATE):
            d, m = xmlDate[0 : 5].split('.')
            w = xmlDate[-1]
            date = datetime.date(self.date.year, int(m), int(d))
            passDate = Easter.dateToStr(Easter.getNearestWeekday(date, int(w)))
            return self.strDate == passDate
        else:
            return False