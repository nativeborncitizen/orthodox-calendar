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


def isStringFitInFormat(s, format):
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
        которая найдена в XML-файле с учетом символа '@'
        вход: дата из XML-файла
        выход: True/False
       """
        dateGroups = xmlDate.split('@')
        return all(map(self.parseDate, dateGroups))

    def parseDate(self, xmlDate):
        """
        Проверка, соответствует ли выбранная дата той,
        которая найдена в XML-файле
        вход: дата из XML-файла
        выход: True/False
       """
        if ':' in xmlDate: # интервал
            return self._parseRange(xmlDate)

        elif isStringFitInFormat(xmlDate, DATE):
            return xmlDate == self.strDate

        elif isStringFitInFormat(xmlDate, EASTER):
            return xmlDate == self.distEaster

        elif isStringFitInFormat(xmlDate, WEEKDAY_AFTER_DATE):
            return self._parseWeekdayAfterDate(xmlDate)

        elif isStringFitInFormat(xmlDate, WEEKDAY_NEAREST_DATE):
            return self._parseWeekdayNearestDate(xmlDate)

        elif isStringFitInFormat(xmlDate, WEEKDAY):
            return self.date.isoweekday() == int(xmlDate[1])

        else:
            return False


    def _parseDateForRange(self, strDate):
        """
        Определение даты для диапазонов дат
        вход: дата в виде дд.мм или En
        выход: дата для года расчетной даты
       """
        if isStringFitInFormat(strDate, DATE):
            return Easter.strToDate(strDate, self.date.year)
        elif isStringFitInFormat(strDate, EASTER):
            return Easter.getDateFromEasterDistance(strDate,
                                                self.date.year)
        else:
            return None

    def _parseRange(self, xmlDate):
        """
        Определение принадлежности даты диапазону
        вход: шаблон диапазона дат дд.мм|En:дд.мм|En
        выход: True/False
       """
        dates = xmlDate.split(':')

        if len(dates) != 2:
            return False

        dateBefore = self._parseDateForRange(dates[0])
        dateAfter = self._parseDateForRange(dates[1])

        if dateBefore is None or dateAfter is None:
            return False

        if dateBefore > dateAfter:
            dateBeforeYear = datetime.date(
                    dateBefore.year - 1, dateBefore.month,
                    dateBefore.day)
            dateAfterYear = datetime.date(
                    dateAfter.year + 1, dateAfter.month,
                    dateAfter.day)
            return dateBeforeYear <= self.date < dateAfter or\
                    dateBefore <= self.date < dateAfterYear
        else:
            return dateBefore <= self.date < dateAfter

    def _parseWeekdayAfterDate(self, xmlDate):
        """
        Определение даты для шаблона типа "дд.мм±н*wд" и года
        расчетной даты
        вход: строка шаблона
        выход: True/False
       """
        day, month, sign, weeks_count, weekday = \
                WEEKDAY_AFTER_DATE.match(xmlDate).groups()

        date = datetime.date(self.date.year,
                                int(month), int(day))

        sign_value = 1 if sign == '+' else -1

        passDate = Easter.dateToStr(
                Easter.getWeekdayFromDate(date,
                    int(weeks_count), int(weekday), sign_value))

        return self.strDate == passDate

    def _parseWeekdayNearestDate(self, xmlDate):
        """
        Определение даты для шаблона типа "дд.мм±н*wд" и года
        расчетной даты
        вход: строка шаблона
        выход: True/False
       """
        day, month, weekday = \
                WEEKDAY_NEAREST_DATE.match(xmlDate).groups()

        date = datetime.date(self.date.year,
                                int(month), int(day))

        passDate = Easter.dateToStr(
                Easter.getNearestWeekday(date, int(weekday)))

        return self.strDate == passDate
