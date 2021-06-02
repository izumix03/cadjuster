from datetime import datetime, timedelta
from enum import Enum

import pytz


class Timezone(Enum):
    TOKYO = 'Asia/Tokyo'


class Datex(object):
    def __init__(self, date):
        self.__date = date

    @classmethod
    def create(cls, timezone):
        return cls(datetime.now(pytz.timezone(timezone.value)))

    def next_weekday(self):
        increase = 1 if self.__date.weekday() != 4 else 3
        return Datex(self.__date + timedelta(days=increase))

    def start(self):
        return Datex(self.__date.replace(hour=0, minute=0, second=0))

    def end(self):
        return Datex(self.__date.replace(hour=23, minute=59, second=59))

    def to_google_date(self):
        return self.__date.astimezone(pytz.timezone('UTC')).replace(tzinfo=None).isoformat() + 'Z'
