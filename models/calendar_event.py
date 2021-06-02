class CalendarEvent(object):

    def __init__(self, my_dict):
        self.summary = ''
        self.attendees = []

        for key in my_dict:
            setattr(self, key, my_dict[key])

    def active(self) -> bool:
        """
        :return:
            自分が参加するイベントならTrue
        """
        return len(self.attendees) > 0 \
               and len(list(filter(lambda e: 'self' in e and e['responseStatus'] == 'accepted', self.attendees))) > 0
