import csv

file = open('Datenbanken/2021-04-26_sps30_sensor_61354.csv', 'r')

csv_daten = csv.reader(file, delimiter=";")

for daten in csv_daten:
    print(f'Zeiten: {daten[5]} Temperatur: {daten[6]}')
