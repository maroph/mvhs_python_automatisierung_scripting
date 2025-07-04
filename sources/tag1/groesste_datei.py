import os

# root_dir = os.path.expanduser('.')
# root_dir = os.path.expanduser('..')
root_dir = os.path.expanduser('~/Downloads')
file_list = []

for root, dirs, files in os.walk(root_dir, topdown=True, onerror=print, followlinks=False):
    # print(f'Aktueller Ordner: {root}')

    for subdir in dirs:
        subdir_path = os.path.join(root, subdir)
        # print(f'  Unterordner: {subdir_path}')

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

file_list.sort(reverse=True)

print('Die 5 größten Dateien sind:')
max_length = 5
if file_list_length < 5:
    max_length = file_list_length
for idx in range(1, max_length + 1):
    size, file_path = file_list[idx]
    print(f'{idx:1}: {size:>10} - {file_path}')
