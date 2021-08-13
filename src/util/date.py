# coding=utf-8

import datetime as dt

def cal_interval_days(d, start_d):
    """calculate interval days from the start date.
        Args:
            d: datetime.date, some date
            start_d: datetime.date, beginning date
        Return:
            n_days: int, interval days """
    #
    delta = d - start_d
    return abs(delta.days)
