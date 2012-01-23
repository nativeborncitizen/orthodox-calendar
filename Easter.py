# -*- coding: utf-8 -*-
import datetime
import re

DATE_OR_EASTER = re.compile('\d\d\.\d\d$|E-?\d+$')

def getEasterDate(year):
    """
    Определение даты Пасхи по формуле К.Ф. Гаусса
    вход: год
    выход: datetime.date по новому стилю
    """
    a = (19 * (year % 19) + 15) % 30
    b = (2 * (year % 4) + 4 * (year % 7) + 6 * a + 6) % 7
    if a + b > 9:
        d = oldToNewStyle(datetime.date(year,  4,  a + b - 9))
    else:
        d = oldToNewStyle(datetime.date(year,  3,  22 + a + b))
        
    LOW_EASTER_RANGE = datetime.date(year,  4,  4)
    HIGH_EASTER_RANGE = datetime.date(year,  5,  8)
    
    if  d < LOW_EASTER_RANGE or d > HIGH_EASTER_RANGE:
        raise EasterOutOfRange
        
    return d
    
def oldToNewStyle(date):
    """
    Перевод из старого стиля в новый
    вход: дата в старом стиле
    выход: дата в новом стиле
    """
    return date + datetime.timedelta(days = 13)
    
def newToOldStyle(date):
    """
    Перевод из нового стиля в старый
    вход: дата в новом стиле
    выход: дата в старом стиле
    """
    return date - datetime.timedelta(days = 13)
    
def dateToReadableStr(date):
    """
    Вывод даты в удобочитаемом виде
    вход: дата
    выход: строка
    """
    Monthes = ["января",  "февраля",  "марта",  "апреля",  "мая",  "июня",  
               "июля",  "августа",  "сентября",  "октября",  "ноября",  "декабря"]
    return "%d %s %d" % (date.day,  Monthes[date.month - 1],  date.year)
    
def dateToStr(date):
    """
    Вывод даты в в формате дд.мм
    вход: дата
    выход: строка
    """
    return date.strftime('%d.%m')

def getEasterDistance(date):
    """
    Определение количества дней до Пасхи
    вход: дата
    выход: строка вида E[-]n
    """
    return 'E%d' % (date - getEasterDate(date.year)).days

def isDate(s):
    """
    Проверка текста на соответствие формату дд.мм или E[-]n
    вход: строка
    выход: True/False
    """
    return DATE_OR_EASTER.match(s) is not None
