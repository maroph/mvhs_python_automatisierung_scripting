#!/usr/bin/env python3
#
####################################################
# Copyright (c) 2025 by Manfred Rosenboom          #
# https://maroph.github.io/ (maroph@pm.me)         #
#                                                  #
# This work is licensed under a CC-BY 4.0 License. #
# https://creativecommons.org/licenses/by/4.0/     #
####################################################
#
import sys
import subprocess


def my_system(argv):
    if not argv:
        # print("argv is None")
        return 1
    if isinstance(argv, str):
        # print("convert string to list:", argv)
        argv = argv.split()
    if not isinstance(argv, list):
        # print("argv is not a list")
        return 1
    if len(argv) == 0:
        # print("len(argv) == 0")
        return 1
    if argv[0] == "":
        # print("argv[0] == \"\"")
        return 1

    # print("run command >>>>>", argv, "<<<<<")
    # print("----------")
    try:
        cp = subprocess.run(argv)
    except FileNotFoundError as e:
        print("my_system:", e)
        return 2
    # print("----------")

    return_code = 0
    try:
        cp.check_returncode()
    except subprocess.CalledProcessError as e:
        return_code = e.returncode
    # print("return_code:", return_code)

    if return_code < 0 or return_code > 255:
        return_code = 1
    return return_code


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('command missing')
        sys.exit(1)

    if len(sys.argv) == 2:
        exitcode = my_system(sys.argv[1])
        sys.exit(exitcode)

    exitcode = my_system(sys.argv[1:])
    sys.exit(exitcode)

