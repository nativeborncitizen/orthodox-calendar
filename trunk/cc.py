#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import getopt
import functools
import church_calendar.calendar_reader
import church_calendar.calendar_locator
import church_calendar.right_date
import church_calendar.console_visualizer
import church_calendar.day_description



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
                church_calendar.calendar_locator.get_calendar_filenames_from_dir, 'xml')

    try:
        opts, args = getopt.getopt(argv[1:], "cf:d:")
    except getopt.GetoptError:
        usage()

    if len(opts) == 1:
        o, a = opts[0]

        if o == "-c":
            getCalendarFilenames = functools.partial(
                church_calendar.calendar_locator.get_calendar_filenames_from_config,
                'cc.ini')
        elif o == "-f":
            getCalendarFilenames = functools.partial(
                church_calendar.calendar_locator.get_calendar_filenames_from_config, a)
        elif o == "-d":
            getCalendarFilenames = functools.partial(
                church_calendar.calendar_locator.get_calendar_filenames_from_dir, a)
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

    dd = church_calendar.day_description.DayDescription(d)

    for filename in getCalendarFilenames():
        try:
            church_calendar.calendar_reader.parseCalendar(filename,
                                          church_calendar.right_date.RightDate(d),  dd)
        except church_calendar.calendar_reader.CalendarFileError:
            pass

    church_calendar.console_visualizer.render(dd)

if __name__ == '__main__':
    main(sys.argv)
