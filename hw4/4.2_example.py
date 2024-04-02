import concurrent.futures
import math
from datetime import datetime
import logging


def split_interval(A, B, n):
    interval_width = (B - A) / n
    return [[A + i * interval_width, A + (i + 1) * interval_width] for i in range(n)]


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    return current_time


def time_logging(func):
    def inner(*args, **kwargs):
        current_time = get_current_time()
        log = f"Beginning Time = {current_time}\n"

        result = func(*args, **kwargs)

        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        
        log += f"params: {args_str} {kwargs_str} result:{result}\n"

        current_time = get_current_time()
        log += f"Ending Time = {current_time}\n"
        logging.info(log)

        return result

    return inner


@time_logging
def integrate(f, a, b, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step

    return acc


def integrate_parallel(f, a, b, n_jobs=1, n_iter=10000000):
    acc = 0
    ni_iter = n_iter // n_jobs + n_iter % n_jobs
    intervals = split_interval(a, b, n_jobs)

    f_list = [f] * n_jobs
    n_iter_list = [ni_iter] * n_jobs
    a_list, b_list = [], []

    for i in range(n_jobs):
        a_list.append(intervals[i][0])
        b_list.append(intervals[i][1])

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        accs = list(executor.map(integrate, f_list, a_list, b_list, n_iter_list))
        acc = sum(accs)

        return acc


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(threadName)s \n%(message)s"
    )

    acc = integrate_parallel(f=math.cos, a=0, b=math.pi / 2, n_jobs=16, n_iter=10000000)
    print(acc)
