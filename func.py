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


def sort_data() -> list:
    """
    Возвращает отсортированный по дате список операций
    :return: list_sort_data
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        data_list = json.load(file)
        format_data = "%Y-%m-%dT%H:%M:%S.%f"
        list_sorted_data = sorted(data_list, key=lambda x: datetime.strptime(x['date'], format_data))
        return list_sorted_data
