#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import getopt
import functools
import Easter
import CalendarReader
import CalendarLocator
import RightDate
import console_visualizer
import day_description



def usage():
    print """cc.py [-c|-f config_file|-d dir_name] [date|-t]

формат даты (date): дд.мм.гггг, по умолчанию дата сегодняшняя
c - список календарей получить из файла cc.ini;
f config_file - список календарей получить из файла с именем config_file;
d dir_name - в качестве списка календарей использовать все xml-файлы из каталога dir_name;
без параметров - по умолчанию -d xml
"""
    sys.exit(2)


def main(argv):
    d = datetime.date.today()
    getCalendarFilenames = functools.partial(
                CalendarLocator.getCalendarFilenamesFromDir, 'xml')

    try:
        opts, args = getopt.getopt(argv[1:], "cf:d:")
    except getopt.GetoptError, err:
        usage()

    if len(opts) == 1:
        o, a = opts[0]

        if o == "-c":
            getCalendarFilenames = functools.partial(
                CalendarLocator.getCalendarFilenamesFromConfig,
                'cc.ini')
        elif o == "-f":
            getCalendarFilenames = functools.partial(
                CalendarLocator.getCalendarFilenamesFromConfig, a)
        elif o == "-d":
            getCalendarFilenames = functools.partial(
                CalendarLocator.getCalendarFilenamesFromDir, a)
        else:
            print "%s - ошибочная опция\n" % o
    elif len(opts) > 1:
        usage()

    if len(args) == 1:
        try:
            d = datetime.datetime.strptime(
                                        args[0], '%d.%m.%Y').date()
            if d.year < 1900:
                raise ValueError
        except ValueError:
            print "Неверная дата\n"
            usage()

    print "%s, %s" % (Easter.getWeekdayStr(d),
                            Easter.dateToReadableStr(d))
    print "(%s ст. ст.)" % Easter.dateToReadableStr(
                            Easter.newToOldStyle(d))

    dd = day_description.DayDescription()

    for filename in getCalendarFilenames():
        try:
            CalendarReader.parseCalendar(filename,
                                          RightDate.RightDate(d),  dd)
        except CalendarReader.CalendarFileError:
            pass

    console_visualizer.render(dd)


if __name__ == '__main__':
    main(sys.argv)
