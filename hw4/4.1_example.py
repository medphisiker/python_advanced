import time
from multiprocessing import Process
from threading import Thread


def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


def run_execution(n):
    start_time = time.time()

    for i in range(10):
        fibonacci(n)

    end_time = time.time()
    return end_time - start_time


def run_threads(n):
    threads = []
    start_time = time.time()

    for i in range(10):
        thread = Thread(target=fibonacci, args=(n,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


def run_processes(n):
    processes = []
    start_time = time.time()

    for i in range(10):
        process = Process(target=fibonacci, args=(n,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    return end_time - start_time


def write_benchmark_report(report_path, messages):
    with open(report_path, "w") as file:
        file.writelines('\n'.join(messages))


if __name__ == "__main__":
    n = 100000
    report_path = "hw4/artifacts/4.1_benchmark_results.txt"

    time_execution = run_execution(n)
    time_threads = run_threads(n)
    time_processes = run_processes(n)

    time_execution_msg = f"Synchronous execution: \t{time_execution} seconds"
    time_threads_msg = f"Threading time: \t{time_threads} seconds"
    time_processes = f"Multiprocessing time: \t{time_processes} seconds"

    messages = (time_execution_msg, time_threads_msg, time_processes)

    for message in messages:
        print(message)

    write_benchmark_report(report_path, messages)
