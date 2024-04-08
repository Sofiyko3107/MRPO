from dataclasses import dataclass


@dataclass(frozen=True)
class Event:

    id: int
    description: str
    influence: str
