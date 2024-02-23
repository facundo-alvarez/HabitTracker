from enum import Enum

class Periodicity(Enum):
    """Enumerates different periodicities for recurring events.

    Defines constants for daily, weekly, monthly, and yearly periodicities.

    Attributes:
        DAILY (int): Represents a daily periodicity (0).
        WEEKLY (int): Represents a weekly periodicity (1).
        MONTHLY (int): Represents a monthly periodicity (2).
        YEARLY (int): Represents a yearly periodicity (3).
    """

    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    YEARLY = 3