import csv

def main():
    print("Welkom in de lees tracker!")
    toon_boekenlijst()
    user_input = input()
    if (user_input == "mb"):
        make_book()

def toon_boekenlijst():
    with open('gebruiker_data/boeken.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            title, author, page_count, isbn, publisher, publication_year, publication_month, publication_day, genre, notes, rating, rating_description = row
            print(row)

def make_book():
    title = input("enter book title")

    with open('gebruiker_data/boeken.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            title, author, page_count, isbn, publisher, publication_year, publication_month, publication_day, genre, notes, rating, rating_description = row

main()