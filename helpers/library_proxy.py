currentLib = None
fun1 = None
fun2 = None
fun3 = None
fun4, fun5, fun6, fun7, fun8, fun9, fun10, fun11, \
    fun12, fun13, fun14, fun15 = [None] * 12
check = None
elseFun = None
combine = None
prepare_input = None


def set_lib(newLib):
    global prepare_input, fun1, fun2, fun3, check, elseFun, combine, currentLib
    global fun4, fun5, fun6, fun7, fun8, fun9, fun10, fun11, \
        fun12, fun13, fun14, fun15
    currentLib = newLib
    prepare_input = newLib.prepare_input
    fun1 = newLib.fun1
    fun2 = newLib.fun2
    fun3 = newLib.fun3
    fun4, fun5, fun6, fun7, fun8, fun9, fun10, fun11, \
        fun12, fun13, fun14, fun15 = [newLib.fun_default] * 12
    check = newLib.check
    elseFun = newLib.elseFun
    combine = newLib.combine


def get_funs():
    return fun1, fun2, fun3, combine, check, elseFun, \
           [fun4, fun5, fun6, fun7, fun8, fun9, fun10, fun11, fun12, fun13,
            fun14, fun15]
