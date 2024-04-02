# Описание

Проект выполняет домашнее задание 4 для курса.

В качестве менеджера зависимостей в проекте выступает `poetry`.

* Скрипт `hw4/4.1_example.py` реализует задачу 4.1
* Модуль `hw4/my_module.py` реализует небольшую библиотеку в виде набора функций для численного интегрирования функции с помощью потоков и процессов.
* Скрипт `hw4/4.2_threads_benchmark.py` реализует задачу 4.2(бенчмарк для потоков), используя модуль `hw4/my_module.py`.
* Скрипт `hw4/4.2_processes_benchmark.py` реализует задачу 4.2(бенчмарк для процессов), используя модуль `hw4/my_module.py`.

Артефакты домашней работы 3 расположены в `hw4/artifacts`:
```
hw4/artifacts
├── 4.1
│   └── 4.1_benchmark_results.txt
└── 4.2
    ├── 4.2_processes_full_info.txt
    ├── 4.2_processes_summary_info.txt
    ├── 4.2_threads_full_info.txt
    └── 4.2_threads_summary_info.txt
```

4.1_benchmark_results.txt - бенчмарк задачи 4.1

4.2_processes_full_info.txt - бенчмарк задачи 4.2 для процессов с подробным логированием.

Содержит логи для каждого отдельного процесса с указанием его PID.
```
2024-04-03 05:58:20,834 - PID process 2509437 
Integration on 2 processes
2024-04-03 05:58:21,076 - PID process 2509441 
Beginning Time = 05:58:20.836394
params: <built-in function cos>, 0.0, 0.7853981633974483, 5000000 result:0.7071068041903416
result:0.7071068041903416
Ending Time = 05:58:21.076135
Execution Time = 0.239741 sec

2024-04-03 05:58:21,080 - PID process 2509442 
Beginning Time = 05:58:20.836395
params: <built-in function cos>, 0.7853981633974483, 1.5707963267948966, 5000000 result:0.29289327434946494
result:0.29289327434946494
Ending Time = 05:58:21.080097
Execution Time = 0.243702 sec

2024-04-03 05:58:21,081 - PID process 2509437 
Integration result = 1.0000000785398064
```
4.2_processes_summary_info.txt - бенчмарк задачи 4.2 для процессов краткий отчет. 

Полезен для оценки влияния числа процессов на время выполнения интегрирования.
```
2024-04-03 05:58:20,343 - PID process 2509437 
Integration on 1 processes
2024-04-03 05:58:20,834 - PID process 2509437 
result:1.0000000785399288
Execution Time = 0.490765 sec

2024-04-03 05:58:20,834 - PID process 2509437 
Integration on 2 processes
2024-04-03 05:58:21,081 - PID process 2509437 
result:1.0000000785398064
Execution Time = 0.246403 sec
```

4.2_threads_full_info.txt - бенчмарк задачи 4.2 для потоков с подробным логированием.

Содержит логи для каждого отдельного потока с указанием его имени.
```
2024-04-03 05:38:49,477 - MainThread 
Integration on 2 threads
2024-04-03 05:38:49,935 - ThreadPoolExecutor-1_0 
Beginning Time = 05:38:49.477284
params: <built-in function cos>, 0.0, 0.7853981633974483, 5000000  result:0.7071068041903416
result:0.7071068041903416
Ending Time = 05:38:49.935603
Execution Time = 0.458319 sec

2024-04-03 05:38:49,951 - ThreadPoolExecutor-1_1 
Beginning Time = 05:38:49.482505
params: <built-in function cos>, 0.7853981633974483, 1.5707963267948966, 5000000  result:0.29289327434946494
result:0.29289327434946494
Ending Time = 05:38:49.951118
Execution Time = 0.468613 sec

2024-04-03 05:38:49,951 - MainThread 
Integration result = 1.0000000785398064
```

4.2_processes_summary_info.txt - бенчмарк задачи 4.2 для потоков краткий отчет. 

Полезен для оценки влияния числа потоков на время выполнения интегрирования.
```
2024-04-03 05:38:49,002 - MainThread 
Integration on 1 threads
2024-04-03 05:38:49,477 - MainThread 
result:1.0000000785399288
Execution Time = 0.474906 sec

2024-04-03 05:38:49,477 - MainThread 
Integration on 2 threads
2024-04-03 05:38:49,951 - MainThread 
result:1.0000000785398064
Execution Time = 0.474265 sec
```
