from models.calendar_event import CalendarEvent
from models.calendar_events import CalendarEvents


class CalendarService(object):

    def __init__(self, service):
        self.__service = service

    def active_events(self, start, end):
        events = [CalendarEvent(e) for e in
                  self.__service.events().list(calendarId='primary',
                                               maxResults=100,
                                               timeMin=start,
                                               timeMax=end,
                                               singleEvents=True,
                                               orderBy='startTime')
                      .execute().get('items', [])
                  ]
        return CalendarEvents(e for e in events if e.active())
