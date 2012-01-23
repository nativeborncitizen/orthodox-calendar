#! /usr/bin/python
# -*- coding: utf-8 -*-

import Easter,  CalendarReader, ConsoleVisualizer,  RightDate, sys,  datetime

CONFIG_FILE = 'cc.ini'

d = datetime.date.today()

if len(sys.argv) > 1:
    try:
        (dd,  mm,  yy) = sys.argv[1].split('.')
        d = datetime.date(int(yy), int(mm), int(dd))
    except:
        print "Неверная дата"
    
CV = ConsoleVisualizer.ConsoleVisualizer()

print Easter.dateToReadableStr(d)
print "(%s ст. ст.)" % Easter.dateToReadableStr(Easter.newToOldStyle(d))
for filename in CalendarReader.getCalendarFilenames(CONFIG_FILE):
    try:
        CalendarReader.parseCalendar(filename, RightDate.RightDate(d),  CV)
    except CalendarReader.CalendarFileError:
        pass
print CV.__str__()


