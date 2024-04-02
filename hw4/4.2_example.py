import concurrent.futures
import math
from datetime import datetime


def split_interval(A, B, n):
    interval_width = (B - A) / n
    return [[A + i * interval_width, A + (i + 1) * interval_width] for i in range(n)]


def integrate(f, a, b, n_iter=1000):   
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"Current Time ={current_time} a={a} b={b} b-a={b - a} n_iter={n_iter}")

    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print(
        f"Current Time ={current_time} a={a} b={b} b-a={b - a} n_iter={n_iter} acc={acc}"
    )
    return acc


def integrate_parallel(f, a, b, n_jobs=1, n_iter=1000):
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
    acc = integrate_parallel(f=math.cos, a=0, b=math.pi / 2, n_jobs=8, n_iter=100000)
    print(acc)
