# -*- coding: utf-8 -*-
"""
Модуль отображения атрибутов праздника в консоли
"""

__author__="nativeborncitizen@blogspot.com"
__date__ ="$1 бер 2012 23:46:38$"

import sys


def render(day_description, file_=sys.stdout):
    """
    Отобразить описание атрибутов праздника из объекта day_description
    в буфер file_ (по умолчанию, консоль)
    """
    print >> file_, "%s\n%s" % (day_description.get_fast().encode('utf-8'),
            '\n'.join([
            text[0].encode('utf-8') for text in day_description.get_texts()])),

if __name__ == "__main__":
    pass
