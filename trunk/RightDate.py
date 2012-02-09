# -*- coding: utf-8 -*-

import datetime
import re

import Easter


# E[-]n
DATE = re.compile('\d\d\.\d\d$')
# E[-]n
EASTER = re.compile('E-?\d+$')
# шаблон для случаев вида "первая суббота по Богоявлении"
WEEKDAY_AFTER_DATE = \
    re.compile('(\d\d)\.(\d\d)([-+])(\d\d)\*w([1-7])')
# шаблон для случаев вида "ближайшее воскресенье к ..."
WEEKDAY_NEAREST_DATE = re.compile('(\d\d)\.(\d\d)~w([1-7])')
# шаблон для дня недели (пост в среду и пятницу)
WEEKDAY = re.compile('w[1-7]')

def isStringFitInFormat(s,  format):
    """
    Проверка текста на соответствие формату
    вход: строка, формат
    выход: True/False
    """
    return format.match(s) is not None


class RightDate:
    """
    Класс для опеределения соответствия текущей даты
    дате из XML-файла
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
        Проверка, соответствует ли выбранная дата той,
        которая найдена в XML-файле с учетом символа '&'
        вход: дата из XML-файла
        выход: True/False
       """
        dateGroups = xmlDate.split('&')
        return all(map(self.parseDate, dateGroups)), \
                    len(dateGroups)

    def parseDate(self, xmlDate):
        """
        Проверка, соответствует ли выбранная дата той,
        которая найдена в XML-файле
        вход: дата из XML-файла
        выход: True/False
       """
        if ':' in xmlDate: # интервал

            dates = xmlDate.split(':')
            l = []

            for date in dates:
                if isStringFitInFormat(date, DATE):
                    l.append(Easter.strToDate(date, self.date.year))
                elif isStringFitInFormat(date, EASTER):
                    l.append(Easter.getDateFromEasterDistance(date,
                                                        self.date.year))
                else:
                    return False

            return l[0] <= self.date <= l[1]

        elif isStringFitInFormat(xmlDate, DATE):
            return xmlDate == self.strDate

        elif isStringFitInFormat(xmlDate, EASTER):
            return xmlDate == self.distEaster

        elif isStringFitInFormat(xmlDate, WEEKDAY_AFTER_DATE):

            day, month, sign, weeks_count, weekday = \
                    WEEKDAY_AFTER_DATE.match(xmlDate).groups()

            date = datetime.date(self.date.year,
                                    int(month), int(day))

            sign_value = 1 if sign == '+' else -1

            passDate = Easter.dateToStr(
                    Easter.getWeekdayFromDate(date,
                        int(weeks_count), int(weekday), sign_value))

            return self.strDate == passDate

        elif isStringFitInFormat(xmlDate, WEEKDAY_NEAREST_DATE):

            day, month, weekday = \
                    WEEKDAY_NEAREST_DATE.match(xmlDate).groups()

            date = datetime.date(self.date.year,
                                    int(month), int(day))

            passDate = Easter.dateToStr(
                    Easter.getNearestWeekday(date, int(weekday)))

            return self.strDate == passDate

        elif isStringFitInFormat(xmlDate, WEEKDAY):
            return self.date.isoweekday() == int(xmlDate[1])


        else:
            return False
