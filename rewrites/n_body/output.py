import multiprocessing as mp
energy_states_0_1_0_sender, energy_states_0_1_0_receiver = mp.Pipe()
energy_states_0_0_1_sender, energy_states_0_0_1_receiver = mp.Pipe()
ctrl_0_0_sender, ctrl_0_0_receiver = mp.Pipe()
solarSystem_0_0_1_1_sender, solarSystem_0_0_1_1_receiver = mp.Pipe()
ctrl_0_1_sender, ctrl_0_1_receiver = mp.Pipe()
solarSystem_0_0_1_2_sender, solarSystem_0_0_1_2_receiver = mp.Pipe()
ctrl_0_2_sender, ctrl_0_2_receiver = mp.Pipe()
energy_0_0_0_sender, energy_0_0_0_receiver = mp.Pipe()
def task_1():
    while True:
        renew = False
        solarSystem_0_0_1_0_1 = solarSystem_0_0_1_2_receiver.recv()
        while not renew:
            sig = ctrl_0_2_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                solarSystem_0_0_1_0_1.advance()
            renew_next_time = sig[0]
            renew = renew_next_time
def task_2():
    a_0_0 = range(0, nIterations)
    while True:
        hasSize = True if hasattr(a_0_0, '__len__') else False
        if hasSize:
            size = len(a_0_0)
            ctrl = True, size
            ctrl_0_0_sender.send(ctrl)
            ctrl = True, size
            ctrl_0_1_sender.send(ctrl)
            ctrl = True, size
            ctrl_0_2_sender.send(ctrl)
        else:
            size = 0
            for d in a_0_0:
                ctrl = False, 1
                ctrl_0_0_sender.send(ctrl)
                ctrl = False, 1
                ctrl_0_1_sender.send(ctrl)
                ctrl = False, 1
                ctrl_0_2_sender.send(ctrl)
                size = size + 1
            ctrl = True, 0
            ctrl_0_0_sender.send(ctrl)
            ctrl = True, 0
            ctrl_0_1_sender.send(ctrl)
            ctrl = True, 0
            ctrl_0_2_sender.send(ctrl)
def task_3():
    while True:
        renew = False
        solarSystem_0_0_1_0_0 = solarSystem_0_0_1_1_receiver.recv()
        while not renew:
            sig = ctrl_0_1_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                energy_0_0_0 = report_energy(solarSystem_0_0_1_0_0)
                energy_0_0_0_sender.send(energy_0_0_0)
            renew_next_time = sig[0]
            renew = renew_next_time
def task_4():
    res = newSystem()
    solarSystem_0_0_1_1_sender.send(res)
    solarSystem_0_0_1_2_sender.send(res)
def task_5():
    energy_states_0_0_1 = []
    energy_states_0_0_1_sender.send(energy_states_0_0_1)
def task_6():
    while True:
        renew = False
        energy_states_0_0_1_0 = energy_states_0_0_1_receiver.recv()
        while not renew:
            sig = ctrl_0_0_receiver.recv()
            count = sig[1]
            for _ in range(0, count):
                var_1 = energy_0_0_0_receiver.recv()
                energy_states_0_0_1_0.append(var_1)
            renew_next_time = sig[0]
            renew = renew_next_time
        energy_states_0_1_0_sender.send(energy_states_0_0_1_0)
from lib import *
def main(nIterations_1):
    global nIterations
    nIterations, = nIterations_1,
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6]
    processes = []
    for task in tasks:
        process = mp.Process(target=task)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = energy_states_0_1_0_receiver.recv()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result