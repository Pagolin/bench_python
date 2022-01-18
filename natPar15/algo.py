import multiprocessing as mp


def task_1(d_0_0_0_sender):
    d_0_0_0 = fun4(i)
    d_0_0_0_sender.send(d_0_0_0)


def task_2(m_0_0_0_sender):
    m_0_0_0 = fun13(i)
    m_0_0_0_sender.send(m_0_0_0)


def task_3(o_0_0_0_sender):
    o_0_0_0 = fun15(i)
    o_0_0_0_sender.send(o_0_0_0)


def task_4(f_0_0_0_sender):
    f_0_0_0 = fun6(i)
    f_0_0_0_sender.send(f_0_0_0)


def task_5(b_0_0_0_sender):
    b_0_0_0 = fun2(i)
    b_0_0_0_sender.send(b_0_0_0)


def task_6(h_0_0_0_sender):
    h_0_0_0 = fun8(i)
    h_0_0_0_sender.send(h_0_0_0)


def task_7(l_0_0_0_sender):
    l_0_0_0 = fun12(i)
    l_0_0_0_sender.send(l_0_0_0)


def task_8(k_0_0_0_sender):
    k_0_0_0 = fun11(i)
    k_0_0_0_sender.send(k_0_0_0)


def task_9(n_0_0_0_sender):
    n_0_0_0 = fun14(i)
    n_0_0_0_sender.send(n_0_0_0)


def task_10(other_i_0_0_0_sender):
    other_i_0_0_0 = fun9(i)
    other_i_0_0_0_sender.send(other_i_0_0_0)


def task_11(j_0_0_0_sender):
    j_0_0_0 = fun10(i)
    j_0_0_0_sender.send(j_0_0_0)


def task_12(result_0_0_0_sender, a_0_0_0_receiver, b_0_0_0_receiver,
            c_0_0_0_receiver, d_0_0_0_receiver, e_0_0_0_receiver,
            f_0_0_0_receiver, g_0_0_0_receiver, h_0_0_0_receiver,
            other_i_0_0_0_receiver, j_0_0_0_receiver, k_0_0_0_receiver,
            l_0_0_0_receiver, m_0_0_0_receiver, n_0_0_0_receiver,
            o_0_0_0_receiver):
    while True:
        var_1 = a_0_0_0_receiver.recv()
        var_2 = b_0_0_0_receiver.recv()
        var_3 = c_0_0_0_receiver.recv()
        var_4 = d_0_0_0_receiver.recv()
        var_5 = e_0_0_0_receiver.recv()
        var_6 = f_0_0_0_receiver.recv()
        var_7 = g_0_0_0_receiver.recv()
        var_8 = h_0_0_0_receiver.recv()
        var_9 = other_i_0_0_0_receiver.recv()
        var_10 = j_0_0_0_receiver.recv()
        var_11 = k_0_0_0_receiver.recv()
        var_12 = l_0_0_0_receiver.recv()
        var_13 = m_0_0_0_receiver.recv()
        var_14 = n_0_0_0_receiver.recv()
        var_15 = o_0_0_0_receiver.recv()
        result_0_0_0 = combine(i, var_1, var_2, var_3, var_4, var_5, var_6,
                               var_7, var_8, var_9, var_10, var_11, var_12,
                               var_13, var_14, var_15)
        result_0_0_0_sender.send(result_0_0_0)


def task_13(c_0_0_0_sender):
    c_0_0_0 = fun3(i)
    c_0_0_0_sender.send(c_0_0_0)


def task_14(a_0_0_0_sender):
    a_0_0_0 = fun1(i)
    a_0_0_0_sender.send(a_0_0_0)


def task_15(e_0_0_0_sender):
    e_0_0_0 = fun5(i)
    e_0_0_0_sender.send(e_0_0_0)


def task_16(g_0_0_0_sender):
    g_0_0_0 = fun7(i)
    g_0_0_0_sender.send(g_0_0_0)


from helpers.library_proxy import *


def main(i_1):
    global i
    i, = i_1,
    result_0_0_0_sender, result_0_0_0_receiver = mp.Pipe()
    o_0_0_0_sender, o_0_0_0_receiver = mp.Pipe()
    n_0_0_0_sender, n_0_0_0_receiver = mp.Pipe()
    m_0_0_0_sender, m_0_0_0_receiver = mp.Pipe()
    l_0_0_0_sender, l_0_0_0_receiver = mp.Pipe()
    k_0_0_0_sender, k_0_0_0_receiver = mp.Pipe()
    j_0_0_0_sender, j_0_0_0_receiver = mp.Pipe()
    other_i_0_0_0_sender, other_i_0_0_0_receiver = mp.Pipe()
    h_0_0_0_sender, h_0_0_0_receiver = mp.Pipe()
    g_0_0_0_sender, g_0_0_0_receiver = mp.Pipe()
    f_0_0_0_sender, f_0_0_0_receiver = mp.Pipe()
    e_0_0_0_sender, e_0_0_0_receiver = mp.Pipe()
    d_0_0_0_sender, d_0_0_0_receiver = mp.Pipe()
    c_0_0_0_sender, c_0_0_0_receiver = mp.Pipe()
    b_0_0_0_sender, b_0_0_0_receiver = mp.Pipe()
    a_0_0_0_sender, a_0_0_0_receiver = mp.Pipe()
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8,
             task_9, task_10, task_11, task_12, task_13, task_14, task_15,
             task_16]
    channels = [[d_0_0_0_sender], [m_0_0_0_sender], [o_0_0_0_sender],
                [f_0_0_0_sender], [b_0_0_0_sender], [h_0_0_0_sender],
                [l_0_0_0_sender], [k_0_0_0_sender], [n_0_0_0_sender],
                [other_i_0_0_0_sender], [j_0_0_0_sender],
                [result_0_0_0_sender, a_0_0_0_receiver, b_0_0_0_receiver,
                 c_0_0_0_receiver, d_0_0_0_receiver, e_0_0_0_receiver,
                 f_0_0_0_receiver, g_0_0_0_receiver, h_0_0_0_receiver,
                 other_i_0_0_0_receiver, j_0_0_0_receiver, k_0_0_0_receiver,
                 l_0_0_0_receiver, m_0_0_0_receiver, n_0_0_0_receiver,
                 o_0_0_0_receiver], [c_0_0_0_sender], [a_0_0_0_sender],
                [e_0_0_0_sender], [g_0_0_0_sender]]
    processes = []
    for task, channels in zip(tasks, channels):
        process = mp.Process(target=task, args=channels)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = result_0_0_0_receiver.recv()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result
