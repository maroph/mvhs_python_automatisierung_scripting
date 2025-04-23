#!/usr/bin/env python3
#
# This script is inspired by the following post:
# *args and **kwargs in Python explained
# https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
#
#
# The names args and kwargs are arbitrary but usually used.
# Important are the * and ** syntax.
#
# *args is used to send a non-keyworded variable length argument list to the function
#     The arguments are passed as an array.
# **kwargs is used to pass keyworded variable length of arguments to a function.
#     The arguments are passed as a dictionary
def func_arg_args_kwargs(arg=None, *args, **kwargs):
    print('arg    :', arg)
    #
    if args is None:
        print('args   : None')
    else:
        if len(args) == 0:
            print('args   : empty list')
        else:
            for a in args:
                print('args   :', a)
    #
    if kwargs is None:
        print('kwargs : None')
    else:
        if len(kwargs) == 0:
            print('kwargs : empty dictionary')
        else:
            # for key, value in sorted(kwargs.items()):
            for key, value in kwargs.items():
                # print("%s == %s" % (key, value))
                print("kwargs : {0} == {1}".format(key, value))
#
#
print('func_arg_args_kwargs(1)')
func_arg_args_kwargs(1)
print()
#
# first with *args
_args = ("two", 3, 5)
print('func_arg_args_kwargs(*_args)')
func_arg_args_kwargs(*_args)
print()
#
#
# now with **kwargs:
_kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
print('func_arg_args_kwargs(**_kwargs)')
func_arg_args_kwargs(**_kwargs)
print()
#
_fargs = 1
_args = (2, 4, 8)
_kwargs = {"arg3": 8, "arg2": 4, "arg1": 2}
print('func_arg_args_kwargs(_fargs, _args, _kwargs)')
func_arg_args_kwargs(_fargs, _args, _kwargs)
print()
print('func_arg_args_kwargs(_fargs, *_args, **_kwargs)')
func_arg_args_kwargs(_fargs, *_args, **_kwargs)
print()
print('func_arg_args_kwargs(_args, _kwargs)')
func_arg_args_kwargs(_args, _kwargs)
print()
print('func_arg_args_kwargs(*_args, **_kwargs)')
func_arg_args_kwargs(*_args, **_kwargs)
print()
print('func_arg_args_kwargs(_kwargs)')
func_arg_args_kwargs(_kwargs)
print()
print('func_arg_args_kwargs(**_kwargs)')
func_arg_args_kwargs(**_kwargs)
print()
print('func_arg_args_kwargs(kwargs=_kwargs)')
func_arg_args_kwargs(kwargs=_kwargs)
print()
print('func_arg_args_kwargs(_fargs, _args)')
func_arg_args_kwargs(_fargs, _args)
print()
print('func_arg_args_kwargs(_fargs)')
func_arg_args_kwargs(_fargs)
print()
print('func_arg_args_kwargs(1, 2, 3)')
func_arg_args_kwargs(1, 2, 3)
print()
