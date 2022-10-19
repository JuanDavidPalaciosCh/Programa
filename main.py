from lab_3 import lab_3
from lab_4 import lab_4
from functions import choose_lab


def main():
    while True:
        lab3 = choose_lab()

        if lab3:
            lab_3()
        else:
            lab_4()


if __name__ == '__main__':
    main()