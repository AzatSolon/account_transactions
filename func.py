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
    n = is_operations_done(i)
    y = sorted(n, key=lambda x: x.get('data'), reverse=True)
