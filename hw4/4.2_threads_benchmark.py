import math
from my_module import create_threads_logger, time_thread_logging, integrate_by_threads


if __name__ == "__main__":
    # integrate setup
    f = math.cos
    a = 0
    b = math.pi / 2
    n_iter = 10**7

    cpu_num = 16
    logger_full = create_threads_logger(
        "4.2 threads full", f"hw4/artifacts/4.2/4.2_threads_full_info.txt"
    )
    logger_summary = create_threads_logger(
        "4.2 threads summary", f"hw4/artifacts/4.2/4.2_threads_summary_info.txt"
    )

    log_summary_info = {
        "start_end": False,
        "func_params": False,
        "result": True,
        "execute_time": True,
    }

    # перебор различного кол-ва потоков
    for n_jobs in range(1, cpu_num * 2 + 1):
        logger_full.info(f"Integration on {n_jobs} threads")
        logger_summary.info(f"Integration on {n_jobs} threads")

        task_func = time_thread_logging(logger_summary, log_summary_info)(
            integrate_by_threads
        )

        acc = task_func(f, a, b, n_jobs, n_iter, logger=logger_full)
        logger_full.info(f"Integration result = {acc}\n")
