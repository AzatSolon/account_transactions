from func import *
from datetime import datetime

five_last_ex = five_last(sort_data(is_operations_done(load_operations())))


def shadow_to(n):
    """
    Функция возвращает замаскuрованный список счетов
    :return:['Счет **0000',...]
    """
    disguise_list = []
    for item in n:
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
    for item in n:
        date = datetime.strptime(item.get("date"), "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
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
    Функция формирует список замаскированных счетов отправитея в случае их отсутствия
    выводит "Открытие вклада"
    :return:
    """
    shadow_list_from = []
    for item in n:
        if item.get("from"):
            shadow = item["from"]
            if "a" in shadow:
                shadow = f"{shadow[:-12]} {shadow[-12:-10]}** **** {shadow[-4:]}"
            else:
                shadow = f"{shadow[:4]} **{shadow[-4:]}"
            shadow_list_from.append(shadow)
        else:
            shadow_list_from.append('Открыте вклада')
    return shadow_list_from


def get_amount(n) -> list:
    """
    Функция возвращает список размера операции и валюту
    :return: ['31234.23 USD', '31234.23 руб',...]
    """
    amount_list = []
    for item in n:
        amount = f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}'
        amount_list.append(amount)
    return amount_list
