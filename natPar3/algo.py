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

def main(i_1):
    global i
    i, = i_1,
    # global  fun1, fun2, fun3, combine
    # fun1, fun2, fun3, combine, *other = library_proxy.get_funs()
    tasks = [task_1, task_2, task_3, task_4]
    processes = []
    for task in tasks:
        process = mp.Process(target=task)
        processes.append(process)
    list(map(mp.Process.start, processes))
    result = result_0_0_0_receiver.recv()
    list(map(mp.Process.terminate, processes))
    list(map(mp.Process.join, processes))
    return result


"""
if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    input = args.Input
    library_proxy.set_lib(lib_select[args.library])
    global fun1, fun2, fun3, combine
    fun1, fun2, fun3, combine, *other = library_proxy.get_funs()
    result = main(input)
    print(result)
"""
