#!/usr/bin/env python
import sys
import pathlib

def main_suma(args):
    result = 0
    for x in args:
        result += int(x)
    return result

def main(args):
    if len(args) != 1:
        print("Usage: cli_args.py FILE_PATH")
        exit(1)
    path = pathlib.Path(args[0])
    if not path.is_file():
        print("Given file does not exits")
        exit(1)
    with path.open() as f:
        size = len(f.read())
    return f"Plik {path} na wielkosc {size}."

if __name__ == '__main__':
    # print(sys.argv)
    print(main(sys.argv[1:]))
