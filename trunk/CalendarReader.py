# -*- coding: utf-8 -*-

import RightDate
import xml.sax
from xml.sax.handler import ContentHandler

class CalendarFileError(Exception):
    pass

MAX_SCORE = 1000 # Вес праздника по умолчанию

class CalendarParser(ContentHandler):
    def __init__(self,  dateTester, visualizer):
        self.dateTester = dateTester
        self.isText = False
        self.isRightDate = False
        self.text = ''
        self.visualizer = visualizer
        self.score = MAX_SCORE
        
    def startElement(self, name, attrs):
        if name == 'day':
            if self.dateTester.isRightDate(attrs.get('date')):
                self.isRightDate = True
        elif name == 'text' and self.isRightDate:
            self.score = int(attrs.get('score',  MAX_SCORE))
            self.isText = True
                    
    def characters(self, ch):
        if self.isText:
            self.text += ch
    
    def endElement(self, name):
        if name == 'text':
            if self.isRightDate:
                self.visualizer.add(self.text,  self.score)
                self.text = ''
            self.isText = False
            
        elif name == 'day':
            self.isRightDate = False
            
def parseCalendar(filename, dateTester, visualizer, open = open):
    """
    Ищет в календаре совпадения с датой из списка дат
    вход: имя xml-файла с календарем и список дат
    выход: строка найденных соответствий
    """
    parser = xml.sax.make_parser()
    Handler = CalendarParser(dateTester, visualizer)
    parser.setContentHandler(Handler)
        
    try:
        parser.parse(open(filename, 'r'))
    except:
        raise CalendarFileError
    

    

    