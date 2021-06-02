class CalendarEvents(object):

    def __init__(self, events):
        self.events = events

    def titles(self):
        return '\n'.join([e.summary for e in self.events])
