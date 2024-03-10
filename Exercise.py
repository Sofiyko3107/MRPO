import Event
import Emotion


class Exercise:
    def __init__(self, date, events, emotions):
        self.date = date
        self.events = events
        self.emotions = emotions

    def get_info(self):

        events = []
        emotions = []

        if self.events:
            for e in self.events:
                events.append(e.get_info())

        if self.emotions:
            for e in self.emotions:
                emotions.append(e.get_info())

        return [self.date, events, emotions]