import multiprocessing as mp


def task_1(d_0_0_0_sender):
    d_0_0_0 = fun4(i)
    d_0_0_0_sender.send(d_0_0_0)


def task_2(result_0_0_0_sender, a_0_0_0_receiver, b_0_0_0_receiver,
           c_0_0_0_receiver, d_0_0_0_receiver):
    while True:
        var_1 = a_0_0_0_receiver.recv()
        var_2 = b_0_0_0_receiver.recv()
        var_3 = c_0_0_0_receiver.recv()
        var_4 = d_0_0_0_receiver.recv()
        result_0_0_0 = combine(i, var_1, var_2, var_3, var_4)
        result_0_0_0_sender.send(result_0_0_0)


def task_3(b_0_0_0_sender):
    b_0_0_0 = fun2(i)
    b_0_0_0_sender.send(b_0_0_0)


def task_4(c_0_0_0_sender):
    c_0_0_0 = fun3(i)
    c_0_0_0_sender.send(c_0_0_0)


def task_5(a_0_0_0_sender):
    a_0_0_0 = fun1(i)
    a_0_0_0_sender.send(a_0_0_0)

from helpers.library_proxy import *

def main(i_1):
    global i
    i, = i_1,
    result_0_0_0_sender, result_0_0_0_receiver = mp.Pipe()
    d_0_0_0_sender, d_0_0_0_receiver = mp.Pipe()
    c_0_0_0_sender, c_0_0_0_receiver = mp.Pipe()
    b_0_0_0_sender, b_0_0_0_receiver = mp.Pipe()
    a_0_0_0_sender, a_0_0_0_receiver = mp.Pipe()
    tasks = [task_1, task_2, task_3, task_4, task_5]
    channels = [[d_0_0_0_sender],
                [result_0_0_0_sender, a_0_0_0_receiver, b_0_0_0_receiver,
                 c_0_0_0_receiver, d_0_0_0_receiver], [b_0_0_0_sender],
                [c_0_0_0_sender], [a_0_0_0_sender]]
    processes = []
    for task, channels in zip(tasks, channels):
        process = mp.Process(target=task, args=channels)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = result_0_0_0_receiver.recv()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result
