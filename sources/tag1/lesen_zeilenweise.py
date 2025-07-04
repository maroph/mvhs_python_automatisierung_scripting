
with open('text.txt', 'r', encoding='utf-8') as f:
    for lineno, line in enumerate(f, start=1):
        print(f'{lineno:2}:', line, end="")
