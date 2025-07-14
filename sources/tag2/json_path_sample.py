import json

def json_path_get_value(json_object: dict, path: str, default_value: dict | list | tuple | str | int | float | bool | None = None) -> tuple[bool, dict | list | tuple | str | int | float | bool | None]:
    """
    Search for a JSON value with an X-Path like expression.

    Parameters:
        json_object (dict)          : JSON object (a Python dictionary).
        path (str)                  : Path expression.
                                      (Sample: /elem1/elem2[2]/elem3)
        default_value (dict | list | tuple | str | int | float | bool | None) :
                                      Default value to return if no value exists.

    Returns:
        tuple[bool, dict | list | tuple | str | int | float | bool | None] :
                                      First item: True if the value exists, False otherwise.
                                      Second item: value found (first item True), otherwise None.
                                      If default_value is not None and no value was found, the
                                      default_value will be returned.
    """
    if json_object is None:
        raise ValueError('json_object is None, but must be a dictionary')
    if type(json_object) is not dict:
        raise ValueError('json_object is not a dictionary')
    if path is None:
        raise ValueError('path is None, but must be a string')
    if type(path) is not str:
        raise ValueError('path is not a string')
    if len(path) < 2:
        raise ValueError('path must be a non-empty string')
    if path[0] != '/':
        raise ValueError('path must begin with a /')

    item = json_object
    for p in path.split('/')[1:]:
        try:
            if not '[' in p:
                item = item[p]
            else:
                arr = p.split('[')
                name = arr[0]
                idx = int(arr[1].split(']')[0])
                item = item[name][idx]
        except KeyError:
            return False, default_value
        except IndexError:
            return False, default_value

    return True, item


if __name__ == '__main__':
    with open("kontakte.json", mode="r", encoding="utf-8") as json_file:
        kontakte = json.load(json_file)

    # print(kontakte)
    # print(json.dumps(kontakte, indent=2, ensure_ascii=False))

    print('---')
    for i in range(0,3):
        print(f'Vorname        : {json_path_get_value(kontakte, f'/kontakte[{i}]/name/vorname', default_value='not set')[1]}')
        print(f'Nachname       : {json_path_get_value(kontakte, f'/kontakte[{i}]/name/nachname', default_value='not set')[1]}')
        plz = json_path_get_value(kontakte, f'/kontakte[{i}]/adresse/plz')
        if plz[0]:
            print(f'PLZ            : {plz[1]}')
        ort_found, ort = json_path_get_value(kontakte, f'/kontakte[{i}]/adresse/ort')
        if ort_found:
            print(f'Ort            : {ort}')
        p_found, p = json_path_get_value(kontakte, f'/kontakte[{i}]/telefon/privat')
        if p_found:
            print(f'Telefon privat : {p}')
        e_found, e = json_path_get_value(kontakte, f'/kontakte[{i}]/email')
        if e_found:
            print(f'E-Mail         : {e}')
        print('---')
