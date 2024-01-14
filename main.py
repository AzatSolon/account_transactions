from func import *
from datetime import datetime

five_last_ex = five_last(sort_data(is_operations_done(load_operations())))


def disguise(accaunt):
    """
    Функция возвращает замаскuрованный список счетов
    :return:['Счет **0000',...]
    """
    disguise_list = []
    for item in accaunt:
        accaunt_sort = item['to']
        accaunt_sort_shadow = f"{accaunt_sort[:4]} **{accaunt_sort[-4:]}"
        disguise_list.append(accaunt_sort_shadow)

    return disguise_list


def date_format(n):
    """
    Функция форматирования даты и возврата списка дат операций
    :return: list ['%d.%m.%Y', '%d.%m.%Y'...]
    """
    format_date_list = []
    for i in n:
        date = datetime.strptime(i.get("date"), "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
        format_date_list.append(date)
    return format_date_list


def get_description(n) -> list:
    """
    Функция формиррует список наименования операции
    :return: list ['','',''...]
    """
    description_list = []
    for item in n:
        description_list.append(item.get("description"))
    return description_list


def shadow_from(n) -> list:
    """
    Функция формирует список счетов отправитея в случае их отсутствия
    выводит "Открытие вклада"
    :return:
    """
    shadow_list_from = []
    for item in n:
        if item.get("from"):
            shadow = item["from"]
            if "a" in shadow:
                shadow = f"{shadow[:-16]}** **** {shadow[-4:]}"
            else:
                shadow = f"{shadow[:4]} **{shadow[-4:]}"
            shadow_list_from.append(shadow)
        else:
            shadow_list_from.append('Открытие вклада')
    return shadow_list_from


if __name__ == '__main__':
    print(shadow_from(five_last_ex))
