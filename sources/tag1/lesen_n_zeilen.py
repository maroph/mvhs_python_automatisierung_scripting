with open('text.txt', 'r', encoding='utf-8') as f:
    count = 1
    while (line := f.readline()) and count <= 2:
        print(f"{count:2}: {line}", end="")
        count += 1
