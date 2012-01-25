#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Утилита компрессии XML-файлов. Предназначена для сбора всех праздников одного дня в один тег
"""

import xml.sax
from xml.sax.handler import ContentHandler

class CalendarFileError(Exception):
    pass

class CalendarParser(ContentHandler):
    def __init__(self):
        self.isDate = False
        self.isText = False
        self.isRightDate = False
        self.date = ''
        self.text = ''
        self.days = {}
        
    def startElement(self, name, attr):
        if name == 'date':
            self.isDate = True
        elif name == 'text':
            self.isText = True
            
    def characters(self, ch):
        if self.isDate:
            self.date += ch
        if self.isText:
            self.text += ch
    
    def endElement(self, name):
        if name == 'date':
            self.isDate = False

        elif name == 'text':
            if self.date in self.days:
                self.days[self.date].append(self.text)
            else:
                self.days[self.date] = [self.text]
            self.text = ''
            self.isText = False
        
        elif name == 'day':
            self.date = ''        
            

parser = xml.sax.make_parser()
Handler = CalendarParser()
parser.setContentHandler(Handler)
    
try:
    parser.parse(open('../calendar.xml', 'r'))
except:
    raise CalendarFileError
    
with open('calendar.xml', 'w') as f:
    f.write("<?xml version='1.0' encoding='utf-8'?>\n<calendar>\n")
    for i in sorted(Handler.days.keys()):
        f.write("\t<day date='%s'>\n" % i)
        for j in Handler.days[i]:
            f.write("\t\t<text>%s</text>\n" % j.encode('utf-8'))
        f.write("\t</day>\n")
    f.write("<\calendar>\n")
