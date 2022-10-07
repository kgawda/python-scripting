import pathlib  # nie ma problemu, ze pliki.py tez importuje pathlib
import pliki
# print(type(pliki))

def main():
    print(pliki)
    print(pliki.main)
    pathlib.Path()

# isntalowanie pip:
# pip install paczka (dla calego systemu)
# pip install paczka (w virtualenv)
# pip install paczka --user

# proxy dla pip (http_proxy, https_proxy)
# Windows: setx http_proxy "http://..."
# Linux: export http_proxy "http://..."


if __name__ == '__main__':
    main()