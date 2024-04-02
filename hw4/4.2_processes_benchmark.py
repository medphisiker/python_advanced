import math
from my_module import (
    create_processes_logger,
    integrate_by_processes,
    time_thread_logging,
)


if __name__ == "__main__":
    # integrate setup
    f = math.cos
    a = 0
    b = math.pi / 2
    n_iter = 10**7

    cpu_num = 16
    logger_full = create_processes_logger(
        "4.2 processes full", f"hw4/artifacts/4.2/4.2_processes_full_info.txt"
    )
    logger_summary = create_processes_logger(
        "4.2 processes summary", f"hw4/artifacts/4.2/4.2_processes_summary_info.txt"
    )

    log_summary_info = {
        "start_end": False,
        "func_params": False,
        "result": True,
        "execute_time": True,
    }

    # перебор различного кол-ва процессов
    for n_jobs in range(1, cpu_num * 2 + 1):
        logger_full.info(f"Integration on {n_jobs} processes")
        logger_summary.info(f"Integration on {n_jobs} processes")

        task_func = time_thread_logging(logger_summary, log_summary_info)(
            integrate_by_processes
        )

        acc = task_func(f, a, b, n_jobs, n_iter, logger=logger_full)
        logger_full.info(f"Integration result = {acc}\n")
