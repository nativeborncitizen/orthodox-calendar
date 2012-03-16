# -*- coding: utf-8 -*-
"""
Модуль отображения атрибутов праздника в консоли
"""

__author__="nativeborncitizen@blogspot.com"
__date__ ="$1 бер 2012 23:46:38$"

import sys
import fasts_and_feasts

# Константы для отображения знаков типикона в консоли по аналогии с
# http://www.canto.ru/calendar/help.php?id=signs
TIPIKON_SIGNS_DISPLAY = {fasts_and_feasts.TIPIKON_SIGNS.FULL_CROSS : "(+)",
        fasts_and_feasts.TIPIKON_SIGNS.HALF_CROSS : "+)",
        fasts_and_feasts.TIPIKON_SIGNS.CROSS : "+",
        fasts_and_feasts.TIPIKON_SIGNS.SLAVOSLOVIE : "[[:.",
        fasts_and_feasts.TIPIKON_SIGNS.SHESTERIK : "[:.",
        fasts_and_feasts.TIPIKON_SIGNS.WITHOUT : ""
}

def render_texts(texts):
    """
    Подготовить строку для вывода из списка праздников с учетом знаков
    типикона
    """
    return '\n'.join([
            "%s %s" % (TIPIKON_SIGNS_DISPLAY[tipikon], text) \
            if tipikon != fasts_and_feasts.TIPIKON_SIGNS.WITHOUT else \
            text for text, tipikon in texts])

def render(day_description, file_=sys.stdout):
    """
    Отобразить описание атрибутов праздника из объекта day_description
    в буфер file_ (по умолчанию, консоль)
    """
    print >> file_, u"%s, %s\n(%s ст. ст.)\n%s\n%s".encode('utf-8') % (
            day_description.get_weekday().encode('utf-8'),
            day_description.get_date().encode('utf-8'),
            day_description.get_old_style_date().encode('utf-8'),
            day_description.get_fast().encode('utf-8'),
            render_texts(day_description.get_texts()).encode('utf-8')
    ),

if __name__ == "__main__":
    pass
