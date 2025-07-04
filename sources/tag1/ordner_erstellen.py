import os

main_dir = 'images'
try:
    os.makedirs(main_dir)
    print(f'Ordner {main_dir} wurde erstellt')
except FileExistsError:
    print(f'Ordner {main_dir} existiert bereits')
except OSError as e:
    print(f'Ordner {main_dir} konnte nicht angelegt werden: {e}')

yy = '25'
for month in range(1,13):
    try:
        sub_dir = f'{main_dir}/{yy}_{month:02}'
        os.makedirs(sub_dir)
        print(f'Ordner {sub_dir} wurde erstellt')
    except FileExistsError:
        print(f'Ordner {sub_dir} existiert bereits')
    except OSError as e:
        print(f'Ordner {sub_dir} konnte nicht angelegt werden: {e}')
