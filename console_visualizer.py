# -*- coding: utf-8 -*-
"""
Модуль отображения атрибутов праздника в консоли
"""

__author__="nativeborncitizen@blogspot.com"
__date__ ="$1 бер 2012 23:46:38$"

import sys
import fasts_and_hollidays

# Константы для отображения знаков типикона в консоли по аналогии с
# http://www.canto.ru/calendar/help.php?id=signs
TIPIKON_SIGNS_DISPLAY = {fasts_and_hollidays.TIPIKON_SIGNS.FULL_CROSS : "(+)",
        fasts_and_hollidays.TIPIKON_SIGNS.HALF_CROSS : "+)",
        fasts_and_hollidays.TIPIKON_SIGNS.CROSS : "+",
        fasts_and_hollidays.TIPIKON_SIGNS.SLAVOSLOVIE : "[[:.",
        fasts_and_hollidays.TIPIKON_SIGNS.SHESTERIK : "[:.",
        fasts_and_hollidays.TIPIKON_SIGNS.WITHOUT : ""
}

def render_texts(texts):
    """
    Подготовить строку для вывода из списка праздников с учетом знаков
    типикона
    """
    return '\n'.join([
            "%s %s" % (TIPIKON_SIGNS_DISPLAY[tipikon], text) \
            if tipikon != fasts_and_hollidays.TIPIKON_SIGNS.WITHOUT else \
            text for text, tipikon in texts])

def render(day_description, file_=sys.stdout):
    """
    Отобразить описание атрибутов праздника из объекта day_description
    в буфер file_ (по умолчанию, консоль)
    """
    print >> file_, "%s\n%s" % (day_description.get_fast().encode('utf-8'),
            render_texts(day_description.get_texts()).encode('utf-8')),

if __name__ == "__main__":
    pass
