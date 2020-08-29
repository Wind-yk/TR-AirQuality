# be careful with the holidays
# at the method is_lective_day()
# 2-21: Carnaval

def to_datetime(a, f="%Y-%m-%d %H:%M"):
    """
    Given string returns datetime object

    Default format of the string: "%Y-%m-%d %H:%M"
    """
    if isinstance(a, datetime):
        pass
    return datetime.strptime(a, f)


def to_text(a, f="%Y-%m-%d %H:%M"):
    """..."""
    return to_datetime(a[:16]).strftime(f)


def to_unix_time(a):
    """..."""
    return to_datetime(a[:16]).timestamp()


def next_days(s, n=1):
    """Given datatime, yield the next n day/s"""
    s = to_datetime(s)
    while True:
        s += timedelta(days=n)
        yield s


def is_lective_day(now):
    """..."""
    now = to_datetime(now)
    return 0 <= now.weekday() < 5


def is_lective_time(now, s_h=8, s_m=0, e_h=14, e_m=40):
    """..."""
    start = datetime.time(s_h,s_m)
    end   = datetime.time(e_h,e_m)
    now   = to_datetime(now).time()
    return start <= now <= end


def is_lective(now):
    """..."""
    return is_lective_day(now) and is_lective_time(now)


def get_lective_days(start, end):
    """..."""
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
