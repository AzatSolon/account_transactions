import json


def load_operations() -> list:
    """
    Возвращает список из файла "operations.json"
    :return: list of operations
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        data_list = json.load(file)
        return data_list


def is_operations_done(i) -> list:
    """
    Возвращает список по ключу "Executed"
    :return: list
    """
    operations_done = []
    for n in i:
        if n.get("state") == "EXECUTED":
            operations_done.append(n)
    return operations_done


def sort_data(i) -> list:
    """
    Возвращает отсортированный по дате список операций
    :return: list_sort_data
    """
    sorted_data = []
    for n in i:
        if n.get("date"):
            sorted_data.append(n)
    sorted_data.sort(key=lambda x: x["date"], reverse=True)
    return sorted_data


def five_last(i) -> list:
    """
    Функция создает саписок 5 последних операций
    :return: five_last_operations = sort_operation_ex[:5]
    """
    five_last_operations = []
    count = 0
    for n in i:
        five_last_operations.append(n)
        count += 1
        if count == 5:
            break
    return five_last_operations
