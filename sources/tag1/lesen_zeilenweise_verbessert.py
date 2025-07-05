
with open('text.txt', 'r', encoding='utf-8') as f:
    count = 1
    while (content := f.readline()):
        print(f'{count}: {content}', end="")
        count += 1
