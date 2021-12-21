import multiprocessing as mp
import time
def itemTask(l):
    time.sleep(1)
    result = l * 2
    return result

def dpar_task(ls, channel):
    innerPool =  mp.Pool()
    results = innerPool.map(itemTask, ls)
    # results = 7
    channel.send(results)


def outer_call(lss):
    channels = [mp.Pipe() for i in range(len(lss))]
    senders = [s for (s,r) in channels]
    receivers = [r for (s,r) in channels]
    procs = []
    for i in range(len(lss)):
        p = mp.Process(target=dpar_task, args=(lss[i],senders[i]))
        p.start()
        procs.append(p)
    results = [r.recv() for r in receivers]
    list(map(mp.Process.terminate, procs))
    list(map(mp.Process.join, procs))
    print(results)


outer_call([list(range(10)), list(range(10,20)), list(range(20, 30))])