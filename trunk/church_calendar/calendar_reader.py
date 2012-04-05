# -*- coding: utf-8 -*-
"""
Модуль парсинга xml-файла с календарем
на основе sax-парсера
"""

import xml.sax
from xml.sax.handler import ContentHandler


class CalendarFileError(Exception):
    """
    Класс-исключение для неправильного формата календаря или
    ошибки открытия файла
    """
    pass


class _CalendarParser(ContentHandler):
    def __init__(self,  dateTester, day_description):
        self.dateTester = dateTester
        self.isText = False
        self.isRightDate = False
        self.priority = 0
        self.text = ''
        self.day_description = day_description
        self.score = self.day_description.MAX_SCORE
        self.tipikon = ''

    def startElement(self, name, attrs):
        if name == 'day':
            self.isRightDate = \
                    self.dateTester.isRightDate(attrs.get('date'))

        elif name == 'text' and self.isRightDate:
            self.score = int(attrs.get(
                    'score',  self.day_description.MAX_SCORE))
            self.tipikon = attrs.get('tipikon',  '')
            self.isText = True

        elif name == 'fast' and self.isRightDate:
            self.day_description.add_fast(
                    attrs.get('type', ''),
                    attrs.get('priority', '0'),
                    bool(attrs.get('polyeley', ''))
            )

    def characters(self, char):
        if self.isText:
            self.text += char

    def endElement(self, name):
        if name == 'text':
            if self.isRightDate:
                self.day_description.add_text(
                        self.text,  self.score, self.tipikon)
                self.text = ''
            self.isText = False

        elif name == 'day':
            self.isRightDate = False


def parseCalendar(filename, dateTester, day_description, open_=open):
    """
    Найти в календаре совпадения с датой из списка дат
    вход: имя xml-файла с календарем и список дат
    выход: строка найденных соответствий
    """
    parser = xml.sax.make_parser()
    Handler = _CalendarParser(dateTester, day_description)
    parser.setContentHandler(Handler)

    try:
        parser.parse(open_(filename, 'r'))
    except:
        raise CalendarFileError





