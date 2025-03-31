#!/usr/bin/env python3
#
##############################################
# Copyright (c) 2025 by Manfred Rosenboom    #
# https://maroph.github.io/ (maroph@pm.me)   #
#                                            #
# This work is licensed under a MIT License. #
# https://choosealicense.com/licenses/mit/   #
##############################################
#
import sys
#
if  __name__ != '__main__':
    print('script must run as a standalone script')
    sys.exit(1)
#
##############################################################################
#
import argparse
import os
#
##############################################################################
#
# adapt the following lines
#
VERSION_NUMBER = 1
VERSION_DATE = '31-MAR-2025'
# help header text
DESCRIPTION='Python3 Script Template'
# help footer text
EPILOG=''
#
##############################################################################
#
SCRIPT_DIR,SCRIPT_NAME = os.path.split(os.path.realpath(sys.argv[0]))
SCRIPT_NAME_BASE = SCRIPT_NAME.split('.py', 2)[0]
VERSION=SCRIPT_NAME_BASE + '  ' + str(VERSION_NUMBER) + '  (' + VERSION_DATE + ')'
#
##############################################################################
#
# create the argument parser
#
parser = argparse.ArgumentParser(prog=SCRIPT_NAME_BASE, description=DESCRIPTION, epilog=EPILOG, allow_abbrev=False)
#
parser.add_argument('-V', '--version', action='version', help='print version information', version=VERSION)
#
##############################################################################
#
# add the needed options
#
#parser.add_argument('-v', '--verbose', help='enable verbose mode', action='store_true')
#
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help='enable verbose mode', action="store_true")
group.add_argument("-q", "--quiet", help='enable quiet mode', action="store_true")
#
parser.add_argument('-n', '--number', help='integer number', type=int)
#
parser.add_argument('-s', '--string', help='string value')
#
##############################################################################
#
# allow further arguments as parameters
#
# 0 or 1 parameter
# parser.add_argument('param', nargs='?', help='parameter', default='')
# 1st mandatory parameter
#parser.add_argument('param1', nargs=1, help='param1')
# 2nd mandatory parameter
#parser.add_argument('param2', nargs=1, help='param2')
# 1 or more parameter(s)
#parser.add_argument('param', nargs='+', help='parameter(s)')
# 0 or more parameter(s)
parser.add_argument('param', nargs='*', help='parameter(s)')
#
##############################################################################
#
# parse the arguments and store the result in args
args = parser.parse_args()
#
params = []
if args.param:
    if len(args.param) > 0:
        params = args.param
#
##############################################################################
#
if args.verbose:
    print('verbose mode is enabled')
else:
    print('verbose mode is disabled')
#
if args.quiet:
    print('quiet mode is enabled')
else:
    print('quiet mode is disabled')
#
if args.number:
    print('value of option number :', args.number)
#
if args.string:
    print('value of option string :', args.string)
#
print('params :', params)

print('')
print('SCRIPT_DIR       :', SCRIPT_DIR)
print('SCRIPT_NAME      :', SCRIPT_NAME)
print('SCRIPT_NAME_BASE :', SCRIPT_NAME_BASE)
print('VERSION          :', VERSION)
print('')

