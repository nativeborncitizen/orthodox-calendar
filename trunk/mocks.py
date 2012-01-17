# -*- coding: utf-8 -*-

class MockFile:
    """
    Mock-объект для тестирования работы с конфигурационными файлами
    вход - строка, содержимое файла
    """
    def __init__(self, s):
        self.s = s.split('\n')
        self.i = 0
    def readline(self):
        if self.i == len(self.s):
            return ''
        else:
            self.i += 1
            return self.s[self.i - 1]
    def sss(self):
        print self.s
