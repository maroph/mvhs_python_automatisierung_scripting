import csv
import sys

# 1. Liste mit Spielergebnissen (jede Zeile als Dictionary)
highscores = [
    {"Spieler": "Nina", "Punkte": 8120, "Level": 5, "Datum": "2025-07-08"},
    {"Spieler": "Tim", "Punkte": 15000, "Level": 7, "Datum": "2025-07-07"},
    {"Spieler": "Alex", "Punkte": 4200, "Level": 3, "Datum": "2025-07-06"}
]

fieldnames = ['Spieler', 'Punkte', 'Level', 'Datum']
dict_writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
dict_writer.writeheader()

dict_writer.writerows(highscores)
# for score in highscores:
#     dict_writer.writerow(score)
