from utils import *


def main():
    """
    Основная функция комбинирует функции проэкта и выводит последние операции
    в требуемом формате.
    :return: "13.11.2019 Перевод со счета на счет
             Счет **9794 -> Счет **8125
             62814.53 руб."
    """
    x = 0
    while x <= 4:
        print(f"{date_format(five_last_ex)[x]} {get_description(five_last_ex)[x]}\n"
              f"{shadow_from(five_last_ex)[x]} -> {shadow_to(five_last_ex)[x]}"
              f"\n{get_amount(five_last_ex)[x]}\n")
        x += 1


if __name__ == '__main__':
    main()
