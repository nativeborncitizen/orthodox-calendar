# -*- coding: utf-8 -*-

import Easter,  CalendarReader, sys,  datetime

d = datetime.date.today()

if len(sys.argv) > 1:
    try:
        (dd,  mm,  yy) = sys.argv[1].split('.')
        d = datetime.date(int(yy), int(mm), int(dd))
    except:
        print "Неверная дата"
    
print Easter.dateToReadableStr(d)
print "(%s ст. ст.)" % Easter.dateToReadableStr(Easter.newToOldStyle(d))
print CalendarReader.parseCalendar('calendar.xml', [Easter.dateToStr(d),  Easter.getEasterDistance(d)])
