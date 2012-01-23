# -*- coding: utf-8 -*-

import RightDate
import xml.sax
from xml.sax.handler import ContentHandler
import ConfigParser

class CalendarFileError(Exception):
    pass

class CalendarParser(ContentHandler):
    def __init__(self,  dateTester, visualizer):
        self.dateTester = dateTester
        self.isDate = False
        self.isText = False
        self.isRightDate = False
        self.date = ''
        self.text = ''
        self.visualizer = visualizer
        
    def startElement(self, name, attr):
        if name == 'date':
            self.isDate = True
        elif name == 'text' and self.isRightDate:
            self.isText = True
            
    def characters(self, ch):
        if self.isDate:
            self.date += ch
        if self.isText:
            self.text += ch
    
    def endElement(self, name):
        if name == 'date':
            if self.dateTester.isRightDate(self.date):
                self.isRightDate = True
            self.date = ''
            self.isDate = False

        elif name == 'text':
            if self.isRightDate:
                self.visualizer.add(self.text)
                self.text = ''
                self.isRightDate = False
            self.isText = False
            
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
    
def getCalendarFilenames(configFile,  open = open):
    Config = ConfigParser.ConfigParser()
    Config.readfp(open(configFile, 'r'))
    return Config.get('Calendar',  'calendars').split(',')
    

    