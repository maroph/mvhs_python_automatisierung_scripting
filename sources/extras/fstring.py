# https://realpython.com/python-f-strings/
# https://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
msg = f"{val}for{val} is a portal for {val}."
print("##", msg)

import datetime

balance = 5425.9292
print(f"Balance: ${balance:.2f}")

heading = "Centered string"
print(f"{heading:=^30}")
msg="Don't Panic!"
print(f'"{msg:<20}"')
print(f'"{msg:^20}"')
print(f'"{msg:>20}"')

date = (9, 6, 2023)
print(f"Date: {date[0]:02}-{date[1]:02}-{date[2]}")

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
print(f"Date: {today:%m/%d/%Y}")

print(f"str(today)  : {today!s}")
print(f"repr(today) : {today!r}")

variable = "Some mysterious value"
print(f"{variable=}")
print(f"{variable = }")
print(f"{variable =}")

dp = 42
print(f"dp : {dp:08}")
print(f"dp : {dp:*>8}")
print(f"dp : {dp:#<8}")

from math import pi
print(f"pi : {pi}")
print(f"pi : {pi:.10f}")
