import helpers.library_proxy as lp
import libs.lib_lists as lib

lp.set_lib(lib)
lp.fun1 = lambda x: x+1
lp.check = lambda x : x % 2 == 0
lp.fun2 = lambda x : [x*i for i in range(x)]
lp.fun3 = lambda x : ["hihi" for _ in range(x)]
import branching.algo as algo_parallel


class Tobject(object):
    def __init__(self, num: int):
        self.num = num

    def method(self):
        return self.num
    def other_method(self):
        return 2*self.num


def algo(i):
    return algo_parallel.main(i)


list_of_tobjects = [Tobject(i) for i in range(4)]
print(algo(10))
