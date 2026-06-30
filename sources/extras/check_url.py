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
import argparse
import os
import requests
import sys


if __name__ != '__main__':
    print('ERROR: runs only as standalone program')
    exit(1)

VERSION_NUMBER = 1
VERSION_DATE = '24-APR-2025'
# help header text
DESCRIPTION = 'check the given URL(s)'
# help footer text
EPILOG = 'Shows the whole redirect chain'
#
##############################################################################
#
SCRIPT_DIR, SCRIPT_NAME = os.path.split(os.path.realpath(sys.argv[0]))
SCRIPT_NAME_BASE = str(SCRIPT_NAME.split('.py', 2)[0])
VERSION = SCRIPT_NAME_BASE + '  ' + str(VERSION_NUMBER) + '  (' + VERSION_DATE + ')'
#
##############################################################################
#
# create the argument parser
#
parser = argparse.ArgumentParser(prog=SCRIPT_NAME_BASE, description=DESCRIPTION, epilog=EPILOG, allow_abbrev=False)
#
parser.add_argument('-V', '--version', action='version', help='print version information', version=VERSION)
parser.add_argument("-n", "--noverifiy", help='TODO', action="store_true")
parser.add_argument('url', nargs='+', help='URL(s) to check')
#
##############################################################################
#
sys.argv.append("--noverifiy")
sys.argv.append("https://de.wikipedia.org/")
# sys.argv.append("https://de.wikipedia.org/")
# sys.argv.append("https://www.google.com")
# sys.argv.append("https://www.google.de")
# sys.argv.append("https://google.de")
# parse the arguments and store the result in args
args = parser.parse_args()
urls = []
if args.url:
    if len(args.url) == 0:
        print('URL(s) missing')
        sys.exit(1)
    urls = args.url
#
##############################################################################
#
# Module requests documentation: https://requests.readthedocs.io/en/master/
# Request/Response documentation:
# https://requests.readthedocs.io/en/master/user/advanced/#request-and-response-objects
# HTTP header infos: https://www.geeksforgeeks.org/http-headers/
#
##############################################################################
#
if args.noverifiy:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

count = 0
errors = 0
for url in urls:
    count += 1
    print('========================================')
    sys.stdout.flush()

    print('URL               :', url)
    try:
        if args.noverifiy:
            resp = requests.head(url=url, allow_redirects=True, headers={'User-Agent': 'check_url/1.0'}, verify=False)
        else:
            resp = requests.head(url=url, allow_redirects=True, headers={'User-Agent': 'check_url/1.0'})
        sys.stdout.flush()
        sys.stderr.flush()
    except Exception as ex:
        print('Error :', ex)
        print('        skip this URL')
        sys.stdout.flush()
        sys.stderr.flush()
        errors += 1
        continue

    if resp is None:
        print('HTTP response object is None')
        sys.stdout.flush()
        errors += 1
        continue

    print('HTTP status code  :', resp.status_code)
    if not resp.ok:
        try:
            resp.raise_for_status()
        except Exception as ex:
            print('HTTP status msg   :', ex)
    print('Elapsed           :', resp.elapsed,
          '(h:mm:ss:milmic, class:datetime.timedelta)')
    print('Links             :', resp.links)
    print('Next              :', resp.next)

    if resp.history:
        print('Redirected        : True')
        for r in resp.history:
            print('Code:', r.status_code)
            print('    Redirected :', str(r.is_redirect).ljust(5, ' '))
            print('    Permanent  :', str(r.is_permanent_redirect).ljust(5, ' '))
            print('    Elapsed    :', r.elapsed)
            print('    URL        :', r.url)
        print('Final URL :', resp.url)
    else:
        print('Redirected        : False')

    print('----------------------------------------')
    print('HTTP response header:')
    dict_headers = {}
    for name, value in resp.headers.items():
        dict_headers[name] = value

    for name in sorted(dict_headers):
        print(f"{name:20s} : {dict_headers[name]}")

    sys.stdout.flush()

print('========================================')
print('URLs processed       :', count)
print('errors in processing :', errors)
sys.stdout.flush()

if errors == len(urls):
    sys.exit(1)
if errors != 0:
    sys.exit(2)
sys.exit(0)
