import os

root_dir = os.path.expanduser('.')
for root, dirs, files in os.walk(root_dir, topdown=True, onerror=print, followlinks=False):
    print(f'Aktueller Ordner: {root}')

    for subdir in dirs:
        subdir_path = os.path.join(root, subdir)
        print(f'  Unterordner: {subdir_path}')

    for filename in files:
        file_path = os.path.join(root, filename)
        print(f'  Datei: {file_path}')
