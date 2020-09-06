import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, time


def to_datetime(t, f="%Y-%m-%d %H:%M"):
    """
    Given string returns datetime object
    Default format of the string: "%Y-%m-%d %H:%M"
    """
    return datetime.strptime(t, f) if isinstance(t, str) else t


def to_text(t, f="%Y-%m-%d %H:%M"):
    """Given datetime, return the string"""
    return t.strftime(f)


def to_unix_time(t):
    """Given datetime, return the unix time."""
    return t.timestamp()


def next_days(s, n=1):
    """Given datatime, yield the next n day/s"""
    s = to_datetime(s)
    while True:
        s += timedelta(days=n)
        yield s


def is_lective_day(now):
    """
    Given the datetime check if `now` is lective.

    (not considering the holidays).
    """
    today = now.weekday()
    return 0 <= today < 5


def is_lective_time(now, s_h=8, s_m=0, e_h=14, e_m=40):
    """
    Given the datetime `now`,
    the start time (s_h, s_m) and the end time (e_h, e_m),
    return whether 'now' is lective time.

    By default, start_time is (8, 0), which represents 8:00,
    and the end time is (14, 40) which represents 14:40.


    INPUT:
        now: datetime
        s_h, s_m: int, meaning start_hour and start_minut
        e_h, e_m: int, meaning end_hour and end_minut
    OUTPUT:
        True or False
    """
    start = time(s_h,s_m)
    end   = time(e_h,e_m)
    now   = now.time()
    return start <= now <= end


def is_lective(now):
    """
    Given the datetime `now`,
    return if it is in lective time.

    INPUT:
        now: datetime
    OUTPUT:
        True or False
    """
    return is_lective_day(now) and is_lective_time(now)


def get_lective_dates(start, end, step=1):
    """
    Given a start and an end (both dates),
    return a list of strings (lective dates)
    with step `step`.

    For instance,
        start = '2020-08-17'
        end   = '2020-08-24'
        step  = 2
    Returns ['2020-8-17', '2020-8-19', '2020-8-21']

    INPUT:
        start, end: str, dates of the form "%Y-%m-%d"
        step: int
    OUTPUT:
        a list of strings that represents lective dates
    """

    assert end >= start and step > 0

    f = "%Y-%m-%d"
    start = to_datetime(start[:10], f)
    end = to_datetime(end[:10], f)

    dates = []
    now = start
    gen = next_days(start, step)
    while now <= end:
        if is_lective_day(now):
            dates.append(to_text(now, f))
        now = next(gen)
    return dates


def get_lective_data(path):
    """..."""
    with open(path, 'r', encoding="UTF-8") as f:
        df = pd.read_csv(f)
        labels = list(df.columns)
        data = []
        for row in list(df.values):
            if is_lective(to_datetime(row[0][:16])):
                data.append(row)
    return labels, data


def plot_and_save(X, Y, stdev, xlabel, ylabel, filename, standard=None):
    """..."""
    plt.gcf().set_size_inches(15, 7)

    plt.plot(X, Y, 'o-')
    if standard is not None:
        plt.hlines(standard, X[0], X[-1], color='r')
    plt.fill_between(X, [Y[i]-stdev[i] for i in range(len(Y))], [Y[i]+stdev[i] for i in range(len(Y))], alpha=0.1)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(filename)
    plt.clf()


def find_hour_day(s, schedule, lective_days):
    """..."""
    dt = to_datetime(s[:16])
    hour = dt.time()
    day = dt.weekday()
    if day in lective_days:
        for i, (start, end) in enumerate(schedule):
            if start <= hour <= end:
                return i, day
    return None
