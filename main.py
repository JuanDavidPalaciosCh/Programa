from lab_3 import lab_3
from functions import choose_lab


def main():
    while True:
        lab3 = choose_lab()

        if lab3:
            lab_3()
        else:
            pass


if __name__ == '__main__':
    main()