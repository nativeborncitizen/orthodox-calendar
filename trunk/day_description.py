# -*- coding: utf-8 -*-
"""
Модуль-контейнер для хранения всех атрибутов дня
"""
import fasts_and_hollidays
import Easter


__author__="nativeborncitizen@blogspot.com"
__date__ ="$1 бер 2012 0:40:17$"

class DayDescription(object):
    """
    Класс-контейнер для хранения информации об атрибутах дня
    """
    MAX_SCORE = 1000 # Вес праздника по умолчанию
    POLYELEY = True # Уточнение строгости поста в полиелейные праздники
    
    def __init__(self, date):
        """
        Инициализация контейнера датой, для которой будет производится
        построение календаря
        """
        self._texts = []
        self._fast = ('np', 0) # по умолчанию нет поста
        self._polyeley_fast = ('', 0)
        self._date = date

    def get_date(self):
        """
        Геттер для даты расчетного дня в читабельном виде
        """
        return Easter.dateToReadableStr(self._date)

    def get_old_style_date(self):
        """
        Определение даты расчетного дня по старому стилю в читабельном виде
        """
        return Easter.dateToReadableStr(
                            Easter.newToOldStyle(self._date))

    def get_weekday(self):
        """
        Определение дня недели расчетного дня
        """
        return Easter.getWeekdayStr(self._date)

    def add_text(self, text,  score,
            tipikon_sign=""):
        """
        Добавление новой строки с описанием праздника
        вход: строка
        вход: вес для сортировки
        вход: знак типикона (по умолчанию, без знака)
        """
        self._texts.append((text,  score,
                fasts_and_hollidays.get_holliday_type(tipikon_sign)))

    def get_texts(self):
        """
        Вернуть список строк описаний праздников, отсортированный по score
        """
        
        return [(text, tipikon) for text, _, tipikon in
                sorted(self._replace_score_on_tipikon(), key = lambda t: t[1])]

    def add_fast(self, fast, priority, polyeley=False):
        """
        Добавить информацию о посте
        указывается тип поста в соответствии с типами, описанными в
        fasts_and_hollidays, приоритет поста и, необязательно, уточнение для
        полиелейных праздников
        """
        def _new_fast(fast_record):
            if priority > fast_record[1]:
                return fast, priority
            else:
                return fast_record

        if polyeley:
            self._polyeley_fast = _new_fast(self._polyeley_fast)
        else:
            self._fast = _new_fast(self._fast)

    def get_fast(self):
        """
        Вернуть описание поста
        """
        if any([tipikon == fasts_and_hollidays.TIPIKON_SIGNS.FULL_CROSS or
                tipikon == fasts_and_hollidays.TIPIKON_SIGNS.HALF_CROSS or
                tipikon == fasts_and_hollidays.TIPIKON_SIGNS.CROSS
                for _, _, tipikon in self._texts
            ]) and self._polyeley_fast[0]:
            return fasts_and_hollidays.get_fast_name(self._polyeley_fast[0])
        else:
            return fasts_and_hollidays.get_fast_name(self._fast[0])

    def _replace_score_on_tipikon(self):
        """
        Вернуть список праздников, в котором, если score не установлен, а есть
        знак типикона, score заменяется на значение знака
        """
        return [(text,
                tipikon if score == self.MAX_SCORE and \
                    tipikon != fasts_and_hollidays.TIPIKON_SIGNS.WITHOUT \
                    else score,
                tipikon)
                for text, score, tipikon in self._texts
                ]

if __name__ == "__main__":
    pass
