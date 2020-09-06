# be careful with the holidays
# at the method is_lective_day()
# 2-21: Carnaval

def to_datetime(t, f="%Y-%m-%d %H:%M"):
    """
    Given string returns datetime object

    Default format of the string: "%Y-%m-%d %H:%M"
    """
    if isinstance(t, datetime):
        pass
    return datetime.strptime(t, f)


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
    Given the datetime (or string, check the method `to_datetime`)
     `now` is lective.

    (not considering the holidays).
    """
    today = to_datetime(now).weekday()
    return 0 <= today < 5


def is_lective_time(now, s_h=8, s_m=0, e_h=14, e_m=40):
    """
    Given datetime or string (check the method 'to_datetime'),
    the start time (s_h, s_m) and the end time (e_h, e_m),
    return whether 'now' is lective time.

    By default, start_time is (8, 0), which represents 8:00,
    and the end time is (14, 40) which represents 14:40.

    (only considers the time, not the day).
    """
    start = datetime.time(s_h,s_m)
    end   = datetime.time(e_h,e_m)
    now   = to_datetime(now).time()
    return start <= now <= end


def is_lective(now):
    """
    Given the datetime or the string `now` (check the method `to_datetime()`),
    Return if it is in lective time.
    """
    return is_lective_day(now) and is_lective_time(now)


def get_dates(start, end, step=1):
    """
    Given a start and an end (both dates),
    return a list of strings with step `step`.

    For instance, for
        start = '2020-01-03'
        end = '2020-01-05'
        step = 2
    Returns ['']
    """
    f = "%Y-%m-%d"
    start = to_datetime(start[:10], f)
    end = to_datetime(end[:10], f)

    dates = []
    now = start
    gen = next_days(start)
    while now <= end:
        if is_lective_day(now):
            dates.append(f'{now.year}-{now.month}-{now.day}')
        now = next(gen)
    return dates


def get_lective_data(path):
    """..."""
    with open(path, 'r', encoding="UTF-8") as f:
        df = pd.read_csv(f)
        columns = list(df.columns)
        data = []
        for row in list(df.values):
            if is_lective(to_datetime(row[0])):
                data.append(row)
    return columns, data

def get_mean(data, labels, n):
    """..."""
    means = dict.fromkeys(labels)
