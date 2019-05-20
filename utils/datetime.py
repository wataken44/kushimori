
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

def get_datetime_from_jst(year, month, day, hour=0, minute=0, second=0, microsecond=0):
    d = datetime(year, month, day, hour, minute, second, microsecond, JST)
    return d.astimezone(timezone.utc)

def utcnow():
    return datetime.now(timezone.utc)


DAY_ZERO = datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
DAY_ONE = datetime(2000, 1, 2, 0, 0, 0, 0, timezone.utc)
DAY_INF = datetime(9999, 12, 31, 23, 59, 59, 0, timezone.utc)
