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

    with path.open() as f:
        for line in f:
            line = line.strip()  # usuwa białe znaki z początku i końca stringa. rstrip() - tylko z końca
            # Opcja
            # if not line or line.startswith('#'):
            #     continue
            print(line)
    # return "Zrobione"

if __name__ == '__main__':
    # print(sys.argv)
    main(sys.argv[1:])