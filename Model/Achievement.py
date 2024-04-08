import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Achievement:

    id: int
    date: datetime.datetime
    description: str

