import codecs
from multiprocessing import Process, Queue
from time import sleep

from my_module import create_processes_logger


def encode_rot13(str):
    return codecs.encode(str, "rot_13")


def process_a(queue_in, queue_out, logger=None):
    while True:
        message = queue_in.get()
        if message != "FINISH":
            lower_message = message.lower()
            if logger:
                logger.info(
                    f"Процесс А\nПрочитано из stdin: {message}\nОтправлено в процесс B: {lower_message}"
                )

            sleep(5)
            queue_out.put(lower_message)
        else:
            queue_out.put("FINISH")
            if logger:
                logger.info(f"Процесс А\nЗавершен")
            break


def process_b(queue_in, queue_out, logger=None):
    while True:
        message = queue_in.get()
        if message != "FINISH":
            encoded_message = encode_rot13(message)
            queue_out.put(encoded_message)

            if logger:
                logger.info(
                    f"Процесс B\nПрочитано из queue_a: {message}\nОтправлено в queue_main: {encoded_message}"
                )
        else:
            if logger:
                logger.info(f"Процесс B\nЗавершен")
            break


if __name__ == "__main__":
    logger = create_processes_logger(
        "4.3_three process_messaging", f"hw4/artifacts/4.3/4.3_processes_full_info.txt"
    )

    # Создаем очереди для обмена между процессами
    queue_main_to_a = Queue()
    queue_a_to_b = Queue()
    queue_b_to_main = Queue()

    process_a = Process(target=process_a, args=(queue_main_to_a, queue_a_to_b, logger))
    process_b = Process(target=process_b, args=(queue_a_to_b, queue_b_to_main, logger))

    process_a.start()
    process_b.start()

    message = ""
    while True and message != "FINISH":
        message = input(
            "Введите сообщение для процесса A или 'FINISH' для завершения: "
        )

        print(message)
        queue_main_to_a.put(message)

        if logger:
            msg = f"Главный процесс\nПользователь ввел: {message}\nОтправил в stdin: {message}"
            logger.info(msg)

    else:
        msg = (
            f"Главный процесс\nЗавершаем программу, ждем остановки процессов А и В...."
        )
        print(msg)
        if logger:
            logger.info(msg)

    process_a.join()
    process_b.join()

    message = f"Главный процесс\nЗавершен."
    print(message)
    logger.info(message)
