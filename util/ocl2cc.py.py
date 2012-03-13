# -*- coding: utf-8 -*-
"""
Скрипт предназначен для конвертации xml-файлов календарей из проекта
http://code.google.com/p/ocl/
"""
import collections
import os
import xml.sax
import datetime
from xml.sax.handler import ContentHandler

__author__="nativeborncitizen@blogspot.com"
__date__ ="$13 бер 2012 22:08:20$"

TIPIKON_SIGNS = {
    'b' : 'FC',
    'v' : 'HC',
    'p' : 'C',
    'g' : 'SL',
    's' : 'SH',
    '' : ''
}

class CalendarFileError(Exception):
    pass

class CalendarParser(ContentHandler):
    def __init__(self):
        self._days = collections.defaultdict(
                lambda:collections.defaultdict(list))
        self._day, self._month = '', ''
        self._isText = False
        self._type, self._sign, self._text = '', '', ''

    def startElement(self, name, attr):
        if name == 'day':
            self._day, self._month = map(int, attr.get('date').split('_'))
            new_style_date = datetime.date(2012, self._month, self._day) + \
                    datetime.timedelta(days = 13)
            self._day, self._month = map(lambda s: "%02d" % s,
                    [new_style_date.day, new_style_date.month])

        elif name == 'group':
            self._isText = True
            self._type, self._sign = \
                    attr.get('type', ''), TIPIKON_SIGNS[attr.get('sign', '')]

    def characters(self, ch):
        if self._isText:
            self._text += ch

    def endElement(self, name):
        if name == 'group':
            self._days[self._month][self._day].append(
                    (self._type, self._sign, self._text))
            self._type, self._sign, self._text = '', '', ''
            self._isText = False

        elif name == 'day':
            self._day, self._month = '', ''

    def get_days(self):
        return self._days

def get_calendar_filenames_from_dir(dir):
    """
    Получить список xml-файлов из указанного каталога
    """
    return map(lambda s: os.path.join(dir, s),
            [file for file in os.listdir(dir) if file.endswith('.xml')])

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    Handler = CalendarParser()
    parser.setContentHandler(Handler)

    for file in get_calendar_filenames_from_dir('../../ocl/clndlib'):
        parser.parse(open(file, 'r'))

    calendar = Handler.get_days()

    with open('_calendar.xml', 'w') as f:
        f.write("<?xml version='1.0' encoding='utf-8'?>\n<calendar>\n")
        for month in sorted(calendar.keys()):
            for day in sorted(calendar[month].keys()):
                f.write("\t<day date='%s.%s'>\n" % (day, month))
                for type, sign, text in calendar[month][day]:
                    if text.encode('utf-8').strip():
                        f.write("\t\t<text type='%s'%s>%s</text>\n" % (
                                type.encode('utf-8'),
                                " tipikon='%s'".encode('utf-8') %
                                        sign if sign else "",
                                text.encode('utf-8').strip()
                        ))
                f.write("\t</day>\n")
        f.write("</calendar>\n")
