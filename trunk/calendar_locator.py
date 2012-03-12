# -*- coding: utf-8 -*-

import os

import ConfigParser

def get_calendar_filenames_from_config(configFile,  open = open):
    """
    Получить список xml-файлов из указанного файла конфигурации
    """
    Config = ConfigParser.ConfigParser()
    Config.readfp(open(configFile, 'r'))
    return Config.get('Calendar',  'calendars').split(',')


def get_calendar_filenames_from_dir(dir):
    """
    Получить список xml-файлов из указанного каталога
    """
    return map(lambda s: os.path.join('xml', s),
               filter(lambda s: s[-3:] == 'xml', os.listdir(dir)))
