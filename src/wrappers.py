import datetime

def time_it(func):
    def wrapper(*args):
        start_time = datetime.datetime.now()
        _ans = func(*args)
        print(f"time elapsed: {datetime.datetime.now() - start_time}")
        return _ans

    return wrapper