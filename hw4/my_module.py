import concurrent.futures
import logging
import math
from datetime import datetime
from functools import wraps


def split_interval(A, B, n):
    """
    Split an interval [A, B] into n equal subintervals.

    Parameters
    ----------
    A : float
        The start of the interval.
    B : float
        The end of the interval.
    n : int
        The number of subintervals to split the interval into.

    Returns
    -------
    list of list of float
        A list of subintervals, where each subinterval is represented as a list of two floats.

    Examples
    --------
    >>> split_interval(0, 10, 5)
    [[0.0, 2.0], [2.0, 4.0], [4.0, 6.0], [6.0, 8.0], [8.0, 10.0]]
    """
    interval_width = (B - A) / n
    return [[A + i * interval_width, A + (i + 1) * interval_width] for i in range(n)]


def time_thread_logging(
    logger,
    log_info={
        "start_end": True,
        "func_params": True,
        "result": True,
        "execute_time": True,
    },
):
    """
    Decorator for logging the execution time and other details of a function.
    This is a special kind of decorator, decorator with parameters.
    (We are made Currying common decorator with a function above).

    This decorator logs the start and end times of the function execution,
    the parameters passed to the function, the result of the function,
    and the total execution time.

    The logging behavior can be customized through the `log_info` dictionary.

    Parameters
    ----------
    logger : logging.Logger
        The logger instance to use for logging.
    log_info : dict, optional
        A dictionary specifying what information to log. The keys can be:
        - "start_end": Whether to log the start and end times (default: True).
        - "func_params": Whether to log the function parameters (default: True).
        - "result": Whether to log the result of the function (default: True).
        - "execute_time": Whether to log the total execution time (default: True).

    Returns
    -------
    Callable
        The decorated function.
    """

    def log_func(func):
        @wraps(func)
        def inner(*args, **kwargs):
            log = ""

            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()

            if log_info["start_end"]:
                start_time_str = start_time.strftime("%H:%M:%S.%f")
                log += f"Beginning Time = {start_time_str}\n"

            if log_info["func_params"]:
                args_str = ", ".join(map(str, args))
                kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
                log += f"params: {args_str} {kwargs_str} result:{result}\n"

            if log_info["result"]:
                log += f"result:{result}\n"

            if log_info["start_end"]:
                end_time_str = end_time.strftime("%H:%M:%S.%f")
                log += f"Ending Time = {end_time_str}\n"

            if log_info["execute_time"]:
                execute_time = (end_time - start_time).total_seconds()
                log += f"Execution Time = {execute_time} sec\n"

            logger.info(log)

            return result

        return inner

    return log_func


def integrate_time_process_logging(
    f,
    a,
    b,
    n_iter,
    logger,
    log_info={
        "start_end": True,
        "func_params": True,
        "result": True,
        "execute_time": True,
    },
):
    """
    Integrates a function over a specified interval and logs the process.

    This function integrates the function `f` over the interval `[a, b]`
    using `n_iter` iterations. It logs the start and end times,
    function parameters, result, and execution time based on the
    `log_info` dictionary.

    Parameters
    ----------
    f : callable
        The function to integrate. It should take a single argument.
    a : float
        The lower limit of the integration interval.
    b : float
        The upper limit of the integration interval.
    n_iter : int
        The number of trapezoids to use for the approximation
    logger : logging.Logger
        The logger instance to use for logging.
    log_info : dict, optional
        A dictionary specifying what information to log. The keys can be:
        - "start_end": Whether to log the start and end times (default: True).
        - "func_params": Whether to log the function parameters (default: True).
        - "result": Whether to log the result of the function (default: True).
        - "execute_time": Whether to log the total execution time (default: True).

    Returns
    -------
    float
        The result of the integration.

    Notes
    -----
    It is a variant of function:
    time_thread_logging(logger_summary, log_summary_info)(integrate_by_threads).

    ProcessPoolExecutor can't pickle decorator function.
    """

    log = ""

    start_time = datetime.now()
    result = integrate(f, a, b, n_iter)
    end_time = datetime.now()

    if log_info["start_end"]:
        start_time_str = start_time.strftime("%H:%M:%S.%f")
        log += f"Beginning Time = {start_time_str}\n"

    if log_info["func_params"]:
        log += f"params: {f}, {a}, {b}, {n_iter} result:{result}\n"

    if log_info["result"]:
        log += f"result:{result}\n"

    if log_info["start_end"]:
        end_time_str = end_time.strftime("%H:%M:%S.%f")
        log += f"Ending Time = {end_time_str}\n"

    if log_info["execute_time"]:
        execute_time = (end_time - start_time).total_seconds()
        log += f"Execution Time = {execute_time} sec\n"

    logger.info(log)

    return result


def integrate(f, a, b, n_iter=10**7):
    """Numerically integrate a function using the trapezoidal rule.

    This function approximates the definite integral of a function from `a` to `b`
    by dividing the area under the curve into `n_iter` trapezoids and summing their
    areas.

    Parameters
    ----------
    f : callable
        The function to integrate. It should take a single argument.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n_iter : int, optional
        The number of trapezoids to use for the approximation, default is 10**7.

    Returns
    -------
    float
        The approximation of the integral of `f` from `a` to `b`.
    """
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step

    return acc


def integrate_by_threads(f, a, b, n_jobs=1, n_iter=10**7, logger=None):
    """
    Numerically integrate a function using the trapezoidal rule in parallel by threads.

    This function approximates the definite integral of a function from `a` to `b`
    by dividing the area under the curve into `n_iter` trapezoids and summing their
    areas in parallel using `n_jobs` threads.

    Parameters
    ----------
    f : callable
        The function to integrate. It should take a single argument.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n_jobs : int, optional
        The number of threads to use for parallel computation, default is 1.
    n_iter : int, optional
        The number of trapezoids to use for the approximation, default is 10**7.
    logger : logging.Logger, optional
        A logger instance for logging, default is None.

    Returns
    -------
    float
        The approximation of the integral of `f` from `a` to `b`.
    """
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
        task_func = time_thread_logging(logger)(integrate)
        accs = list(executor.map(task_func, f_list, a_list, b_list, n_iter_list))
        acc = sum(accs)

        return acc


def integrate_by_processes(f, a, b, n_jobs=1, n_iter=10**7, logger=None):
    """
    Numerically integrate a function using the trapezoidal rule in parallel by processes.

    This function approximates the definite integral of a function from `a` to `b`
    by dividing the area under the curve into `n_iter` trapezoids and summing their
    areas in parallel using `n_jobs` processes.

    Parameters
    ----------
    f : callable
        The function to integrate. It should take a single argument.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n_jobs : int, optional
        The number of processes to use for parallel computation, default is 1.
    n_iter : int, optional
        The number of trapezoids to use for the approximation, default is 10**7.
    logger : logging.Logger, optional
        A logger instance for logging, default is None.

    Returns
    -------
    float
        The approximation of the integral of `f` from `a` to `b`.
    """
    acc = 0
    ni_iter = n_iter // n_jobs + n_iter % n_jobs
    intervals = split_interval(a, b, n_jobs)

    f_list = [f] * n_jobs
    n_iter_list = [ni_iter] * n_jobs
    loggers = [logger] * n_jobs
    a_list, b_list = [], []

    for i in range(n_jobs):
        a_list.append(intervals[i][0])
        b_list.append(intervals[i][1])

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        accs = list(
            executor.map(
                integrate_time_process_logging,
                f_list,
                a_list,
                b_list,
                n_iter_list,
                loggers,
            )
        )
        acc = sum(accs)

        return acc


def create_threads_logger(logger_name, log_file_path):
    """Create a logger with a file handler for thread-specific logging.

    This function sets up a logger with a file handler that formats log messages
    to include the timestamp, thread name, and the log message itself. The logger
    is configured to log messages with a severity level of INFO or higher.

    Parameters
    ----------
    logger_name : str
        The name of the logger. This is used to retrieve or create a logger
        instance.
    log_file_path : str
        The path to the log file where the log messages will be written.

    Returns
    -------
    logger : logging.Logger
        A logger instance configured with the specified name and file handler.
    """
    logger = logging.getLogger(logger_name)

    file_handler = logging.FileHandler(log_file_path, "w")
    formatter = logging.Formatter("%(asctime)s - %(threadName)s \n%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)
    return logger


def create_processes_logger(logger_name, log_file_path):
    """Create a logger with a file handler for parallel processes specific logging.

    This function sets up a logger with a file handler that formats log messages
    to include the timestamp, process ID, and the log message itself. The logger
    is configured to log messages with a severity level of INFO or higher.

    Parameters
    ----------
    logger_name : str
        The name of the logger. This is used to retrieve or create a logger
        instance.
    log_file_path : str
        The path to the log file where the log messages will be written.

    Returns
    -------
    logger : logging.Logger
        A logger instance configured with the specified name and file handler.
    """
    logger = logging.getLogger(logger_name)

    file_handler = logging.FileHandler(log_file_path, "w")
    formatter = logging.Formatter("%(asctime)s - PID process %(process)s \n%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)
    return logger
