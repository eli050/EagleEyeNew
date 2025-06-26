from enum import Enum

class Status(Enum):
    ACTIVE = "active"
    INJURED = "injured"
    MISSING = "missing"
    RETIRED = "retired"

    def __str__(self):
        return self.value