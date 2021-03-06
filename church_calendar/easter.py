# -*- coding: utf-8 -*-

import datetime


DAYS_IN_A_WEEK = 7
DAYS_IN_A_YEAR = 365
DAYS_IN_A_LEAP_YEAR = 364

def get_Easter_date(year):
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

    assert(d >= LOW_EASTER_RANGE and d <= HIGH_EASTER_RANGE)

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
    Monthes = [u"января", u"февраля", u"марта", u"апреля",
               u"мая", u"июня", u"июля", u"августа", u"сентября",
               u"октября",  u"ноября",  u"декабря"]
    return "%d %s %d" % (date.day,  Monthes[date.month - 1],
                            date.year)


def dateToStr(date):
    """
    Вывод даты в в формате дд.мм
    вход: дата
    выход: строка
    """
    return date.strftime('%d.%m')


def strToDate(s, year):
    """
    Получение даты из "дд.мм" и года
    вход: строка "дд.мм"
    вход: год
    выход: дата
    """
    return datetime.date(year, int(s[3:]), int(s[:2]))


def getEasterDistanceFromDate(date):
    """
    Определение количества дней до Пасхи
    вход: дата
    выход: строка вида E[-]n
    """
    return 'E%d' % (date - get_Easter_date(date.year)).days


def getDateFromEasterDistance(dist, year):
    """
    Определение даты по количеству дней до Пасхи
    вход: строка вида E[-]n
    вход: год
    выход: дата
    """
    return get_Easter_date(year) + datetime.timedelta(days =
                                                     int(dist[1:]))


def getWeekdayFromDate(d, n, w, s):
    """
    Определение даты n-ого дня недели до или после даты
    вход: d - дата, от которой ведется рассчет
    вход: n - какой по счету день недели после указанного
    вход: w - какой день недели (понедельник - 1)
    вход: s - 1 или -1 - до или после
    выход: дата
    """
    weekDayOfHoliday = d.isoweekday()

    if s > 0:
        dist = getWeekdayAfterDist(weekDayOfHoliday, w)
    else:
        dist = getWeekdayBeforeDist(weekDayOfHoliday, w)

    weeks = (n - 1) * DAYS_IN_A_WEEK

    dist += weeks

    return d + s * datetime.timedelta(days = dist)


def getNearestWeekday(d, w):
    """
    Определение даты ближайшего к дате дня недели
    вход: d - дата, от которой ведется рассчет
    вход: w - какой день недели (понедельник - 1)
    выход: дата
    """
    weekDayOfHoliday = d.isoweekday()

    after = getWeekdayAfterDist(weekDayOfHoliday, w)
    before = getWeekdayBeforeDist(weekDayOfHoliday, w)

    if after > before:
        dist = -before
    elif after == before:
        dist = 0
    else:
        dist = after

    return d + datetime.timedelta(days = dist)


def getWeekdayStr(d):
    """
    Определение дня недели в удобочитаемом виде
    вход: строка
    """
    return [u'Понедельник', u'Вторник', u'Среда', u'Четверг',
                u'Пятница', u'Суббота', u'Воскресенье'][d.weekday()]


def getWeekdayAfterDist(d, a):
    """
    Определение расстояния до следующего дня недели
    вход: текущий день недели, искомый день недели
    выход: расстояние в днях
    """
    if d < a:
        return a - d
    else:
        return DAYS_IN_A_WEEK - d + a


def getWeekdayBeforeDist(d, b):
    """
    Определение расстония до предідущего дня недели
    вход: текущий день недели, искомый день недели
    выход: расстояние в днях
    """
    if d > b:
        return d - b
    else:
        return d + DAYS_IN_A_WEEK - b

def shiftDateOnYear(date, years):
    """
    Определение даты сдвинутой на указанное количество лет.
    Если 29.02 сдвигается не на високосный год, выбрасывается
    ValueError
    вход: дата
    вход: количество лет для сдвига (может быть < 0)
    выход: сдвинутая дата
    """
    return datetime.date(date.year + years, date.month,
            date.day)


def get_voice(date):    
    '''
    Определение гласа для указаной даты
    '''
    Easter_date = get_Easter_date(date.year)
    
    if date < Easter_date:
        Easter_date_before = get_Easter_date(date.year - 1)
        Easter_date_after = Easter_date
    else:
        Easter_date_before = Easter_date 
        Easter_date_after = get_Easter_date(date.year + 1)
        
    if Easter_date_before <= date < \
            Easter_date_before + datetime.timedelta(days = 7) or \
            Easter_date_after - datetime.timedelta(days = 7) <= date < \
            Easter_date_after:
        return None
    
    return (((date - Easter_date_before).days - 7) // 7) % 8 + 1


def get_week_after_Easter(date):
    '''
    Определение номера недели после Пасхи
    '''
    year = date.year - 1 if date <= get_Easter_date(date.year) else date.year
    return (date - get_Easter_date(year)).days // 7 + 1


