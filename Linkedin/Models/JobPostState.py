from enum import Enum

class JobState(Enum):
    OPEN = 1,
    BLOCKED = 2,
    CLOSED = 3
