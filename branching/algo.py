import multiprocessing as mp


def task_1(e_0_0_sender, current_0_0_0_2_receiver, ctrlTrue_0_receiver):
    while True:
        renew = False
        current_0_0_0_0 = current_0_0_0_2_receiver.recv()
        while not renew:
            sig = ctrlTrue_0_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                e_0_0 = fun2(current_0_0_0_0)
                e_0_0_sender.send(e_0_0)
            renew_next_time = sig[0]
            renew = renew_next_time


def task_2(ctrl_0_0_sender, d_1_sender):
    b_0_0 = range(i)
    while True:
        hasSize = True if hasattr(b_0_0, '__len__') else False
        if hasSize:
            size = len(b_0_0)
            ctrl = True, size
            ctrl_0_0_sender.send(ctrl)
            for d in b_0_0:
                d_1_sender.send(d)
        else:
            size = 0
            for d in b_0_0:
                d_1_sender.send(d)
                ctrl = False, 1
                ctrl_0_0_sender.send(ctrl)
                size = size + 1
            ctrl = True, 0
            ctrl_0_0_sender.send(ctrl)


def task_3(flag_0_0_0_sender, c1_0_0_0_receiver):
    while True:
        var_0 = c1_0_0_0_receiver.recv()
        flag_0_0_0 = fun1(var_0)
        flag_0_0_0_sender.send(flag_0_0_0)


def task_4(result_0_0_1_sender):
    result_0_0_1 = []
    result_0_0_1_sender.send(result_0_0_1)


def task_5(result_2_sender, c_0_0_1_receiver, e_0_0_receiver, f_0_0_receiver):
    while True:
        branchSelection = c_0_0_1_receiver.recv()
        if branchSelection:
            result = e_0_0_receiver.recv()
            result_2_sender.send(result)
        else:
            result = f_0_0_receiver.recv()
            result_2_sender.send(result)


def task_6(c_0_0_0_sender, c_0_0_1_sender, flag_0_0_0_receiver):
    while True:
        var_0 = flag_0_0_0_receiver.recv()
        res = check(var_0)
        c_0_0_0_sender.send(res)
        c_0_0_1_sender.send(res)


def task_7(c1_0_0_0_sender, c2_0_0_0_sender, d_1_receiver):
    while True:
        var_0 = d_1_receiver.recv()
        res = double(var_0)
        c1_0_0_0 = res[0]
        c1_0_0_0_sender.send(c1_0_0_0)
        c2_0_0_0 = res[1]
        c2_0_0_0_sender.send(c2_0_0_0)


def task_8(ctrlTrue_0_sender, ctrlFalse_0_sender, c_0_0_0_receiver):
    while True:
        branchSelection = c_0_0_0_receiver.recv()
        if branchSelection:
            ctrlTrue = True, 1
            ctrlFalse = True, 0
            ctrlTrue_0_sender.send(ctrlTrue)
            ctrlFalse_0_sender.send(ctrlFalse)
        else:
            ctrlTrue = True, 0
            ctrlFalse = True, 1
            ctrlTrue_0_sender.send(ctrlTrue)
            ctrlFalse_0_sender.send(ctrlFalse)


def task_9(current_0_0_0_2_sender, current_0_0_0_3_sender, c2_0_0_0_receiver):
    while True:
        var_0 = c2_0_0_0_receiver.recv()
        res = fun1(var_0)
        current_0_0_0_2_sender.send(res)
        current_0_0_0_3_sender.send(res)


def task_10(f_0_0_sender, current_0_0_0_3_receiver, ctrlFalse_0_receiver):
    while True:
        renew = False
        current_0_0_0_1 = current_0_0_0_3_receiver.recv()
        while not renew:
            sig = ctrlFalse_0_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                f_0_0 = fun3(current_0_0_0_1)
                f_0_0_sender.send(f_0_0)
            renew_next_time = sig[0]
            renew = renew_next_time


def task_11(result_0_1_0_sender, result_0_0_1_receiver, ctrl_0_0_receiver,
            result_2_receiver):
    while True:
        renew = False
        result_0_0_1_0 = result_0_0_1_receiver.recv()
        while not renew:
            sig = ctrl_0_0_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                var_1 = result_2_receiver.recv()
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
    c1_0_0_0_sender, c1_0_0_0_receiver = mp.Pipe()
    c2_0_0_0_sender, c2_0_0_0_receiver = mp.Pipe()
    flag_0_0_0_sender, flag_0_0_0_receiver = mp.Pipe()
    c_0_0_0_sender, c_0_0_0_receiver = mp.Pipe()
    current_0_0_0_2_sender, current_0_0_0_2_receiver = mp.Pipe()
    ctrlTrue_0_sender, ctrlTrue_0_receiver = mp.Pipe()
    current_0_0_0_3_sender, current_0_0_0_3_receiver = mp.Pipe()
    ctrlFalse_0_sender, ctrlFalse_0_receiver = mp.Pipe()
    f_0_0_sender, f_0_0_receiver = mp.Pipe()
    e_0_0_sender, e_0_0_receiver = mp.Pipe()
    c_0_0_1_sender, c_0_0_1_receiver = mp.Pipe()
    result_2_sender, result_2_receiver = mp.Pipe()
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8,
             task_9, task_10, task_11]
    channels = [[e_0_0_sender, current_0_0_0_2_receiver, ctrlTrue_0_receiver],
                [ctrl_0_0_sender, d_1_sender],
                [flag_0_0_0_sender, c1_0_0_0_receiver], [result_0_0_1_sender],
                [result_2_sender, c_0_0_1_receiver, e_0_0_receiver,
                 f_0_0_receiver],
                [c_0_0_0_sender, c_0_0_1_sender, flag_0_0_0_receiver],
                [c1_0_0_0_sender, c2_0_0_0_sender, d_1_receiver],
                [ctrlTrue_0_sender, ctrlFalse_0_sender, c_0_0_0_receiver],
                [current_0_0_0_2_sender, current_0_0_0_3_sender,
                 c2_0_0_0_receiver],
                [f_0_0_sender, current_0_0_0_3_receiver, ctrlFalse_0_receiver],
                [result_0_1_0_sender, result_0_0_1_receiver, ctrl_0_0_receiver,
                 result_2_receiver]]
    processes = []
    for task, channels in zip(tasks, channels):
        process = mp.Process(target=task, args=channels)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = result_0_1_0_receiver.recv()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result
