from scr.func import *


test_list = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
  },
  {
    "id": 41428829,
    "state": "CANCELED",
    "date": "2019-07-03T18:35:29.512364"
  }
]


def test_sort_data():
    assert sort_data(test_list) == [
        {
            'date': '2019-08-26T10:50:58.294041',
            'id': 441945886,
            'state': 'EXECUTED'},
        {
            'date': '2019-07-03T18:35:29.512364',
            'id': 41428829,
            'state': 'CANCELED'
        }
    ]


def test_operations_done():
    assert operations_done(test_list) == [{'date': '2019-08-26T10:50:58.294041', 'id': 441945886, 'state': 'EXECUTED'}]


def test_five_last():
    assert len(five_last(test_list)) <= 5
