# Python's F-String for String Interpolation and Formatting
# https://realpython.com/python-f-strings/
#
# https://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
# 20-NOV-2025

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
msg = f"{val}for{val} is a portal for {val}."
print("##", msg)

import datetime

balance = 5425.9292
print(f"Balance: ${balance:.2f}")
print()
heading = "Centered string"
print(f"{heading:^30}")
print(f"{heading:=^30}")
print()

msg="Don't Panic!"
print(f'"{msg:<20}"')
print(f'"{msg:^20}"')
print(f'"{msg:>20}"')
print()

date = (9, 6, 2023)
print(f"Date: {date[0]:02}-{date[1]:02}-{date[2]}")

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
print(f"Date: {today:%m/%d/%Y}")
print()

print(f"str(today)  : {today!s}")
print(f"repr(today) : {today!r}")
print()

variable = "Some mysterious value"
print(f"{variable=}")
print(f"{variable = }")
print(f"{variable =}")
print()

dp = 42
print(f"dp : {dp:08}")
print(f"dp : {dp:*>8}")
print(f"dp : {dp:#<8}")
print()

from math import pi
print(f"pi : {pi}")
print(f"pi : {pi:.10f}")
print()

# =====================================================================
# =====================================================================

# Upgrading F-Strings: Python 3.12 and Beyond
# https://realpython.com/python-f-strings/#upgrading-f-strings-python-312-and-beyond

sample_dict = {"key": "value"}

# Works for all Python 3 versions
print(f"value: {sample_dict['key']}")
print(f'value: {sample_dict["key"]}')
print()

# Works for Python 3.12 or higher
print(f"value: {sample_dict["key"]}")
print(f'value: {sample_dict['key']}')
