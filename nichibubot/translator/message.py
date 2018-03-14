import re


class Message:
    def __init__(self, text):
        self._text = self._normalize_text(text)
        self._intent = None
        self._recipient = None
        self._task = None
        self._date = None
        self._location = None
        self._entity = None

    @staticmethod
    def _remove_non_words(mess):
        reg = re.compile('[,.!?*_~`\t\n]')
        return reg.sub('', mess)

    def _normalize_text(self, mess):
        mess = mess.strip()
        mess = mess.lower()
        mess = self._remove_non_words(mess)
        return mess

    @property
    def text(self):
        return self._text

    @property
    def intent(self):
        return self._intent

    @property
    def recipient(self):
        return self._recipient

    @property
    def task(self):
        return self._task

    @property
    def date(self):
        return self._date

    @property
    def entity(self):
        return self._entity

    @property
    def location(self):
        return self._location

    def set_intent(self, intent):
        self._intent = intent
        return self

    def set_recipient(self, recipient):
        self._recipient = recipient
        return self

    def set_task(self, task):
        self._task = task
        return self

    def set_location(self, location):
        self._location = location
        return self

    def set_date(self, date):
        self._date = date
        return self

    def set_entity(self, entity):
        self._entity = entity
        return self
