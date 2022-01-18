import multiprocessing as mp

result_0_1_0_q = mp.Queue()
result_0_0_1_q = mp.Queue()
ctrl_0_0_q = mp.Queue()
d_1_q = mp.Queue()
x_0_0_0_q = mp.Queue()
y_0_0_0_q = mp.Queue()
z_0_0_0_q = mp.Queue()
queues = [result_0_1_0_q, result_0_0_1_q, ctrl_0_0_q,
          d_1_q, x_0_0_0_q, y_0_0_0_q, z_0_0_0_q]


def task_1():
    while True:
        var_0 = d_1_q.get()
        x_0_0_0 = fun1(var_0)
        x_0_0_0_q.put(x_0_0_0)


def task_2():
    while True:
        var_0 = y_0_0_0_q.get()
        z_0_0_0 = fun3(var_0)
        z_0_0_0_q.put(z_0_0_0)


def task_3():
    while True:
        var_0 = x_0_0_0_q.get()
        y_0_0_0 = fun2(var_0)
        y_0_0_0_q.put(y_0_0_0)


def task_4():
    a_0_0 = range(0, i)
    while True:
        hasSize = True if hasattr(a_0_0, '__len__') else False
        if hasSize:
            size = len(a_0_0)
            ctrl = True, size
            ctrl_0_0_q.put(ctrl)
            for d in a_0_0:
                d_1_q.put(d)
        else:
            size = 0
            for d in a_0_0:
                d_1_q.put(d)
                ctrl = False, 1
                ctrl_0_0_q.put(ctrl)
                size = size + 1
            ctrl = True, 0
            ctrl_0_0_q.put(ctrl)


def task_5():
    result_0_0 = []
    result_0_0_1_q.put(result_0_0)


def task_6():
    while True:
        renew = False
        result_0_0_1_0 = result_0_0_1_q.get()
        while not renew:
            sig = ctrl_0_0_q.get()
            count = sig[1]
            for _ in range(0, count):
                var_1 = z_0_0_0_q.get()
                print("new z", var_1)
                result_0_0_1_0.append(var_1)
            renew_next_time = sig[0]
            renew = renew_next_time
            print("current result", result_0_0_1_0)
        result_0_1_0_q.put(result_0_0_1_0)
        print("result send")


from loop3.lib_pipeline import *


def main(i_1):
    global i
    i, = i_1,
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6]
    processes = []
    for task in tasks:
        process = mp.Process(target=task)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = result_0_1_0_q.get()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result
