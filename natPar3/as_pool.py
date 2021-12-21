import multiprocessing as mp

result_0_0_0_sender, result_0_0_0_receiver = mp.Pipe()
z_0_0_0_sender, z_0_0_0_receiver = mp.Pipe()
y_0_0_0_sender, y_0_0_0_receiver = mp.Pipe()
x_0_0_0_sender, x_0_0_0_receiver = mp.Pipe()


def task_1():
    while True:
        var_0 = x_0_0_0_receiver.recv()
        var_1 = y_0_0_0_receiver.recv()
        var_2 = z_0_0_0_receiver.recv()
        result_0_0_0 = combine(i, var_0, var_1, var_2)
        result_0_0_0_sender.send(result_0_0_0)


def task_2():
    y_0_0_0 = fun2(i)
    y_0_0_0_sender.send(y_0_0_0)


def task_3():
    z_0_0_0 = fun3(i)
    z_0_0_0_sender.send(z_0_0_0)


def task_4():
    x_0_0_0 = fun1(i)
    x_0_0_0_sender.send(x_0_0_0)


from helpers.library_proxy import *


def algo(i_1):
    global i
    i, = i_1,
    tasks = [task_1, task_2, task_3, task_4]
    num_workers = len(tasks) if len(tasks)<=16 else 16
    pool = mp.Pool(num_workers)
    results = []
    for task in tasks:
        results.append(pool.apply_async(task))
    result = result_0_0_0_receiver.recv()
    pool.terminate()
    pool.join()
    return result
