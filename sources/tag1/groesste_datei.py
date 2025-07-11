import os
import sys

root_dir = os.path.expanduser('.')
# root_dir = os.path.expanduser('..')
# root_dir = os.path.expanduser('~/Downloads')
file_list = []

for root, dirs, files in os.walk(root_dir, topdown=True, onerror=print, followlinks=False):
    for filename in files:
        file_path = os.path.join(root, filename)
        try:
            size = os.path.getsize(file_path)
        except OSError:
            size = -1
        # print(f'  Datei: {file_path} , size: {size}')
        file_list.append((size, file_path))

print(f'Durchsuchter Ordner: {root_dir}')
file_list_length = len(file_list)
print(f'Anzahl Dateien: {file_list_length}')

if file_list_length < 1:
    print('Keine Dateien gefunden')
    sys.exit(0)

print()

file_list.sort(reverse=True)

print('Die 5 größten Dateien sind (Größe in Bytes):')
max_length = 5
if file_list_length < 5:
    max_length = file_list_length

idx = 1
for size, file_path in file_list[:max_length]:
    print(f'{idx:1}: {size:>10} - {file_path}')
    idx = idx + 1
