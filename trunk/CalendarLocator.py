import os

import ConfigParser

def getCalendarFilenamesFromConfig(configFile,  open = open):
    Config = ConfigParser.ConfigParser()
    Config.readfp(open(configFile, 'r'))
    return Config.get('Calendar',  'calendars').split(',')


def getCalendarFilenamesFromDir(dir):
    return map(lambda s: os.path.join('xml', s),
               filter(lambda s: s[-3:] == 'xml', os.listdir(dir)))
