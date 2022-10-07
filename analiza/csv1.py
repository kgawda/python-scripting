#!/usr/bin/env python
import sys
import pathlib

# Pobranie sciezki do pliku, jak w cli_argv.py
# Otworzenie tego pliku i przejechanie petla for po wszystkich linijkach tego pliku
#    (wydrukowanie kazdej linijki osobno) - jak w pliki.py
# Testujemy z:
# https://people.sc.fsu.edu/~jburkardt/data/csv/mlb_players.csv

def main(args):
    # Opcja - sprawdzane czy podano argument
    if len(args) != 1:
        print(f"Usage: {sys.argv[0]} FILE_PATH")
        exit(1)

    path = pathlib.Path(args[0])

    # Opcja - sprawdzanie czy plik istnieje
    if not path.is_file():
        print("Given file does not exits")
        exit(1)

    # Liczymy sredni wiek zawodnika
    # -> pominac pierwsza linijke (enumerate)
    # -> podzielic linijke na elementy (str.split)
    # -> pominac linijki ktore nie maja 6 elementow

    age_sum = 0
    counter = 0
    with path.open() as f:
        with open("output.csv", "w") as output:
            for line_number, line in enumerate(f):
                if line_number == 0:
                    continue
                line = line.strip()  # usuwa białe znaki z początku i końca stringa. rstrip() - tylko z końca
                # Opcja
                # if not line or line.startswith('#'):
                #     continue
                elements = line.split(", ")
                if len(elements) != 6:
                    continue

                # zrzucamy kolumny 1 i 6 do osobnego pliku:
                output.write(f"{elements[0]}, {elements[5]}\n")

                age_sum += float(elements[5])
                counter += 1
    print(f"Sredni wiek {age_sum/counter:.2f}")


    # return "Zrobione"

if __name__ == '__main__':
    # print(sys.argv)
    main(sys.argv[1:])