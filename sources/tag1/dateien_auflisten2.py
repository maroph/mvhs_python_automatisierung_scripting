import os

dir = '.'
with open('diritems2.out.txt', 'w', encoding='utf-8') as f:
    for diritem in os.listdir(dir):
        diritem_path = os.path.join('.', diritem)
        if os.path.isdir(diritem_path):
            f.write(f"d : {diritem}\n")
        elif os.path.isfile(diritem_path):
            f.write(f"f : {diritem}\n")
        else:
            f.write(f"- : {diritem}\n")
