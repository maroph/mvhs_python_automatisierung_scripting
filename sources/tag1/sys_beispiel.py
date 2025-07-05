import sys

print(f'Python Version (sys.version) : {sys.version}')
print('---')
for idx, val in enumerate(sys.argv):
    print(f'sys.argv[{idx}]: {val}')

sys.exit(0)
