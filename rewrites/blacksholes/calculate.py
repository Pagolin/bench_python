import multiprocessing as mp
results_0_1_0_sender, results_0_1_0_receiver = mp.Pipe()
results_0_0_1_sender, results_0_0_1_receiver = mp.Pipe()
ctrl_0_0_sender, ctrl_0_0_receiver = mp.Pipe()
d_0_0_sender, d_0_0_receiver = mp.Pipe()
n_0_0_0_sender, n_0_0_0_receiver = mp.Pipe()
def task_1():
    while True:
        var_0 = d_0_0_receiver.recv()
        n_0_0_0 = calulateForOption(var_0)
        n_0_0_0_sender.send(n_0_0_0)
def task_2():
    valOps_0_0_0 = refl(ops)
    while True:
        data = valOps_0_0_0
        hasSize = True if hasattr(data, '__len__') else False
        if hasSize:
            size = len(data)
            ctrl = True, size
            ctrl_0_0_sender.send(ctrl)
            for d in data:
                d_0_0_sender.send(d)
        else:
            size = 0
            for d in data:
                d_0_0_sender.send(d)
                ctrl = False, 1
                ctrl_0_0_sender.send(ctrl)
                size = size + 1
            ctrl = True, 0
            ctrl_0_0_sender.send(ctrl)
def task_3():
    results_0_0_1 = list()
    results_0_0_1_sender.send(results_0_0_1)
def task_4():
    while True:
        renew = False
        results_0_0_1_0 = results_0_0_1_receiver.recv()
        while not renew:
            sig = ctrl_0_0_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                var_1 = n_0_0_0_receiver.recv()
                results_0_0_1_0.append(var_1)
            renew_next_time = sig[0]
            renew = renew_next_time
        results_0_1_0_sender.send(results_0_0_1_0)
from bs_lib import (calulateForOption, refl)
def main(ops_1):
    global ops
    ops, = ops_1,
    tasks = [task_1, task_2, task_3, task_4]
    processes = []
    for task in tasks:
        process = mp.Process(target=task)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = results_0_1_0_receiver.recv()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result