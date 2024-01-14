from scr.utils import *

test_list = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
]


def test_shadow_to():
    assert shadow_to(test_list) == ['Счет **9589', 'Счет **5560']


def test_shadow_from():
    assert shadow_from(test_list) == ['Maestro 1596 83** **** 5199', 'MasterCard 7158 30** **** 6758']


def test_date_format():
    assert date_format(test_list) == ['26.08.2019', '03.07.2019']


def test_get_description():
    assert get_description(test_list) == ['Перевод организации', 'Перевод организации']


def test_get_amount():
    assert get_amount(test_list) == ['31957.58 руб.', '8221.37 USD']

