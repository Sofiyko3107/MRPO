from dataclasses import dataclass


@dataclass(frozen=True)
class Emotion:

    id: int
    emotionType: str
    intensity: int
