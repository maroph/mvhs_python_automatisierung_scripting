from datetime import datetime
import os
from pathlib import Path

PERM_DICT = {
    '0': '---',
    '1': '--x',
    '2': '-w-',
    '3': '-wx',
    '4': 'r--',
    '5': 'r-x',
    '6': 'rw-',
    '7': 'rwx'
}

def simple_ls(directory_name: str | None = None, reverse: bool = False, recursive: bool = False) -> None:
    if directory_name is None or directory_name == '':
        path = Path('.')
    else:
        path = os.path.expanduser(Path(directory_name))

    diritems = sorted(os.listdir(path), reverse=reverse)
    directories = []
    if recursive:
        print(f'{path}:')
    for diritem in diritems:
        diritem_path = os.path.join(path, diritem)
        diritem_stat = os.stat(diritem_path)

        if os.path.isdir(diritem_path):
            directories.append(diritem) if recursive else None
            diritem_type = 'd'
        else:
            diritem_type = '-'

        perm_number = str(oct(diritem_stat.st_mode))[-3:]
        permissions = ""
        for d in perm_number:
            permissions += PERM_DICT[d]

        dt = datetime.fromtimestamp(float(str(diritem_stat.st_ctime)))
        # time = dt.strftime("%b %d %Y %H:%M:%S")
        time = dt.strftime('%Y-%m-%dT%H:%M:%S')

        print(f'{diritem_type}{permissions} {diritem_stat.st_size:>10} {time} {diritem}')

    if recursive:
        for d in directories:
            print()
            return simple_ls(os.path.join(path, d), reverse=reverse, recursive=recursive)

    return None

if __name__ == '__main__':
    simple_ls()
    # simple_ls('.')
    # simple_ls('..', recursive=True)
    # simple_ls('..', reverse=True, recursive=True)
