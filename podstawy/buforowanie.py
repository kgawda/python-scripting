import time
import sys

def main():
    for _ in range(10):
        print('.', end='')
        # Jak unikacn buforowania?
        # Opcja: sys.stdout.flush()
        time.sleep(0.5)
    print()

if __name__ == '__main__':
    main()

# Inne opcje:
# python -u buforowanie.py
# Windows: set PYTHONUNBUFFERED=1
# Linux: export PYTHONUNBUFFERED=1