import datetime
from dataclasses import dataclass, field

from Model.Event import Event
from Model.Emotion import Emotion


@dataclass
class Exercise:

    id: int
    date: datetime.datetime
    events: list[Event] = field(default_factory=list)
    emotions: list[Emotion] = field(default_factory=list)

    def __eq__(self, other):
        return self.id == other.id and self.date == other.date
