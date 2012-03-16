# -*- coding: utf-8 -*-

import os

import ConfigParser

def get_calendar_filenames_from_config(configFile,  open_ = open):
    """
    Получить список xml-файлов из указаного файла конфигурации
    """
    Config = ConfigParser.ConfigParser()
    Config.readfp(open_(configFile, 'r'))
    return Config.get('Calendar',  'calendars').split(',')


def get_calendar_filenames_from_dir(dir_):
    """
    Получить список xml-файлов из указаного каталога
    """
    return map(lambda s: os.path.join('xml', s),
               filter(lambda s: s[-3:] == 'xml', os.listdir(dir_)))
