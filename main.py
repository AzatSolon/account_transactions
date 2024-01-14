from utils import *


def main():
    x = 0
    while x <= 4:
        print(f"{date_format(five_last_ex)[x]} {get_description(five_last_ex)[x]}\n"
              f"{shadow_from(five_last_ex)[x]} -> {shadow_to(five_last_ex)[x]}"
              f"\n{get_amount(five_last_ex)[x]}\n")
        x += 1


if __name__ == '__main__':
    main()
