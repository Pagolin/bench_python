"""
usual library_proxy doesn't fit realy well to the branching case, which needs
'double', 'id_fun', 'if_fun', 'else_fun' and 'check'
"""

currentLib = None
double = lambda x : (x, x)
id_fun = lambda x : x
prepare_input = id_fun
if_fun = None
else_fun = None
check = None



def set_lib(newLib):
    global prepare_input, double, id_fun, if_fun, check, else_fun,currentLib
    currentLib = newLib
    prepare_input = newLib.prepare_input
    check = newLib.check
    if_fun = newLib.if_fun
    else_fun = newLib.else_fun


def get_funs():
    return prepare_input, id_fun, double, check, if_fun, else_fun
