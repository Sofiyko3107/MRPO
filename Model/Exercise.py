import datetime
from dataclasses import dataclass, field

from Model.Event import Event
from Model.Emotion import Emotion

@dataclass
class Exercise:

    def __init__(self, id: int, date: datetime.datetime, events: list[Event], emotions: list[Emotion]):
        self.id = id
        self.date = date
        self.events = events
        self.emotions = emotions

    def __eq__(self, other):
        return self.id == other.id and self.date == other.date
