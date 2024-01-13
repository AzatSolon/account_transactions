import json
from datetime import datetime


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
    format_data = "%Y-%m-%dT%H:%M:%S.%f"
    list_sorted_data = sorted(i, key=lambda x: datetime.strptime(x['date'], format_data))
    return list_sorted_data
