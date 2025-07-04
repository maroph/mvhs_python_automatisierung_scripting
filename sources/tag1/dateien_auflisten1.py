import os

dir = '.'
with open('diritems1.out.txt', 'w', encoding='utf-8') as f:
    for diritem in os.listdir(dir):
        f.write(f"{diritem}\n")
