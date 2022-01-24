import multiprocessing as mp


def task_1(x_0_0_0_sender, d_1_receiver):
    while True:
        var_0 = d_1_receiver.recv()
        x_0_0_0 = fun1(var_0)
        x_0_0_0_sender.send(x_0_0_0)


def task_2(z_0_0_0_sender, y_0_0_0_receiver):
    while True:
        var_0 = y_0_0_0_receiver.recv()
        z_0_0_0 = fun3(var_0)
        z_0_0_0_sender.send(z_0_0_0)


def task_3(y_0_0_0_sender, x_0_0_0_receiver):
    while True:
        var_0 = x_0_0_0_receiver.recv()
        y_0_0_0 = fun2(var_0)
        y_0_0_0_sender.send(y_0_0_0)


def task_4(ctrl_0_0_sender, d_1_sender):
    a_0_0 = range(0, i)
    while True:
        hasSize = True if hasattr(a_0_0, '__len__') else False
        if hasSize:
            size = len(a_0_0)
            ctrl = True, size
            ctrl_0_0_sender.send(ctrl)
            for d in a_0_0:
                d_1_sender.send(d)
        else:
            size = 0
            for d in a_0_0:
                d_1_sender.send(d)
                ctrl = False, 1
                ctrl_0_0_sender.send(ctrl)
                size = size + 1
            ctrl = True, 0
            ctrl_0_0_sender.send(ctrl)


def task_5(result_0_0_1_sender):
    result_0_0_1 = []
    result_0_0_1_sender.send(result_0_0_1)


def task_6(result_0_1_0_sender, result_0_0_1_receiver, ctrl_0_0_receiver,
           z_0_0_0_receiver):
    while True:
        renew = False
        result_0_0_1_0 = result_0_0_1_receiver.recv()
        while not renew:
            sig = ctrl_0_0_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                var_1 = z_0_0_0_receiver.recv()
                result_0_0_1_0.append(var_1)
            renew_next_time = sig[0]
            renew = renew_next_time
        result_0_1_0_sender.send(result_0_0_1_0)


from helpers.library_proxy import *


def main(i_1):
    global i
    i, = i_1,
    result_0_1_0_sender, result_0_1_0_receiver = mp.Pipe()
    result_0_0_1_sender, result_0_0_1_receiver = mp.Pipe()
    ctrl_0_0_sender, ctrl_0_0_receiver = mp.Pipe()
    d_1_sender, d_1_receiver = mp.Pipe()
    x_0_0_0_sender, x_0_0_0_receiver = mp.Pipe()
    y_0_0_0_sender, y_0_0_0_receiver = mp.Pipe()
    z_0_0_0_sender, z_0_0_0_receiver = mp.Pipe()
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6]
    channels = [[x_0_0_0_sender, d_1_receiver],
                [z_0_0_0_sender, y_0_0_0_receiver],
                [y_0_0_0_sender, x_0_0_0_receiver],
                [ctrl_0_0_sender, d_1_sender], [result_0_0_1_sender],
                [result_0_1_0_sender, result_0_0_1_receiver, ctrl_0_0_receiver,
                 z_0_0_0_receiver]]
    processes = []
    for task, channels in zip(tasks, channels):
        process = mp.Process(target=task, args=channels)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = result_0_1_0_receiver.recv()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result
