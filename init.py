import csv

def main():
    print("Welkom in de lees tracker!")
    toon_boekenlijst()

def toon_boekenlijst():
    with open('gebruiker_data/boeken.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            titel, schrijver, aantal_paginas = row
            print(f"{titel} van {schrijver} met {aantal_paginas} pagina's")

main()