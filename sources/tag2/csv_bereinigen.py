import csv
from pathlib import Path

path_input = Path('./csv-dateien')
path_output = Path('./csv-output')

# path_output.unlink(missing_ok=True)
path_output.mkdir(parents=True, exist_ok=True)

for path_item in path_input.iterdir():
    if path_item.is_file():
        if path_item.suffix.lower() == '.csv':
            print(f'Lese Datei {path_item}')
            try:
                with open(path_item, encoding='utf-8', newline='') as f:
                    reader = csv.reader(f)
                    next(reader)
                    rows = [row for row in reader]
            except StopIteration:
                continue
            print('Datei gelesen')

            print()

            csv_file_out = Path(path_output, path_item.name)
            print(f'Schreibe Datei {csv_file_out}')
            with open(csv_file_out, mode="w", encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print('Datei geschrieben')

            print('---')
