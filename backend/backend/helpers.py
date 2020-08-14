from datetime import datetime
from typing import Tuple

date_range = Tuple[datetime.date, datetime.date]

def date_range_intersect(range_a: date_range, range_b: date_range) -> date_range:
    start_a, end_a = range_a
    start_b, end_b = range_b

    if start_a is None:
        new_start_date = start_b
    elif start_b is None:
        new_start_date = start_a
    elif start_a > start_b:
        new_start_date = start_a
    else:
        new_start_date = start_b

    if end_a is None:
        new_end_date = end_b
    elif end_b is None:
        new_end_date = end_a
    elif end_a < end_b:
        new_end_date = end_a
    else:
        new_end_date = end_b

    return new_start_date, new_end_date
