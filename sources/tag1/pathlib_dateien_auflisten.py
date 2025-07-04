from pathlib import Path

dir = '.'
start_path = Path(dir)
for path_item in start_path.iterdir():
    if path_item.is_dir():
        print(f"d : {path_item.name}")
    elif path_item.is_file():
        print(f"f : {path_item.name}")
    else:
        print(f"- : {path_item.name}")
