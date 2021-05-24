from enum import Enum


class BillingPeriod(Enum):

    INSTANT = "instant"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    MONTHLY = "monthly"
