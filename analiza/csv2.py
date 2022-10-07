#!/usr/bin/env python
import sys
import pathlib
import csv

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
        with open("output2.csv", "w") as output:
            reader = csv.reader(f, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
            writer = csv.writer(output, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if len(row) != 6:
                    continue
                print(row)
                #writer.writerow(row)
                writer.writerow([row[0], row[5]])

if __name__ == '__main__':
    main(sys.argv[1:])