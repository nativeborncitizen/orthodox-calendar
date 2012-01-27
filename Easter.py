# -*- coding: utf-8 -*-
import datetime

DAYS_IN_A_WEEK = 7

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

def getWeekdayAfterDate(d, n, w):
    """
    Определение даты n-ого дня недели после даты
    вход: d - дата, от которой ведется рассчет
    вход: n - какой по счету день недели после указанного
    вход: w - какой день недели (понедельник - 1)
    выход: дата
    """
    weekDayOfHoliday = d.isoweekday()
    if weekDayOfHoliday < w:
        dist = w - weekDayOfHoliday
    else:
        dist = DAYS_IN_A_WEEK - weekDayOfHoliday + w
    weeks = (n - 1) * DAYS_IN_A_WEEK
    dist += weeks
    return d + datetime.timedelta(days = dist)

def getWeekdayBeforeDate(d, n, w):
    """
    Определение даты n-ого дня недели перед датой
    вход: d - дата, от которой ведется рассчет
    вход: n - какой по счету день недели после указанного
    вход: w - какой день недели (понедельник - 1)
    выход: дата
    """
    weekDayOfHoliday = d.isoweekday()
    if weekDayOfHoliday > w:
        dist = weekDayOfHoliday - w
    else:
        dist = weekDayOfHoliday + DAYS_IN_A_WEEK - w
    weeks = (n - 1) * DAYS_IN_A_WEEK
    dist += weeks
    return d - datetime.timedelta(days = dist)

def getWeekdayStr(d):
    """
    Определение дня недели в удобочитаемом виде
    вход: строка
    """
    return ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'][d.weekday()]
