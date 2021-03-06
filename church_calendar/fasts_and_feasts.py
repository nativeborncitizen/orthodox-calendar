# -*- coding: utf-8 -*-
"""
Описание основных постов и праздников
"""

# обозначения типа поста в xml-файле
FASTS = { "st" : "Строгий пост".decode('utf-8'),
           "ol" :
        "Разрешена пища с раститительным маслом".decode('utf-8'),
           "ik" : "Разрешена икра".decode('utf-8'),
           "fi" : "Разрешена рыба".decode('utf-8'),
           "mm" : "Запрет на мясо".decode('utf-8'),
           "np" : "Нет поста".decode('utf-8')
         }

def get_fast_name(code):
    """
    Определение типа поста
    вход: строка, код поста
    выход: строка, определение ограничений поста
    """
    return FASTS[code] if code in FASTS else ''

def enum(**enums):
    """Определение перечислимого типа как в
    http://stackoverflow.com/questions/36932/whats-the-best-way-to-implement-an-enum-in-python
    """
    return type('Enum', (), enums)

# знаки Типикона
TIPIKON_SIGNS = enum(FULL_CROSS = 12, # бдение на великие праздники
        HALF_CROSS = 100, # бдение
        CROSS = 200, # с полиелеем
        SLAVOSLOVIE = 300, # со славословием
        SHESTERIK = 500, # на шесть
        WITHOUT = 1000)

# обозначения знаков Типикона в xml-файле
TIPIKON_XML = {"FC" : TIPIKON_SIGNS.FULL_CROSS,
        "HC" : TIPIKON_SIGNS.HALF_CROSS,
        "C" : TIPIKON_SIGNS.CROSS,
        "SL" : TIPIKON_SIGNS.SLAVOSLOVIE,
        "SH" : TIPIKON_SIGNS.SHESTERIK}

def get_holliday_type(tipikon_xml_attr):
    """Вернуть значение типа праздника на основании атрибута tipikon
    в xml-файле
    """
    return TIPIKON_XML[tipikon_xml_attr] if tipikon_xml_attr in TIPIKON_XML \
        else TIPIKON_SIGNS.WITHOUT
