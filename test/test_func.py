from function import func
from function import operations_cl


def test_slice_last_operation():
    assert func.slice_last_operation([1, 2, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]


def test_add_stars_card():
    assert func.add_stars_card("carta 12345678900987654321") == "carta 1234 56** **** 4321"
    assert func.add_stars_card("Счет 12345678900987654321") == "Счет **4321"
    assert func.add_stars_card("card card") == "card card"


def test_add_star_to_chek():
    assert  func.add_star_to_chek("счет 555555555") == "Счет **5555"


def test_make_list_opration_object():
    json = [{
             "id": 957763565,
             "state": "EXECUTED",
             "date": "2019-01-05T00:52:30.108534",
             "operationAmount": {
                 "amount": "87941.37",
                 "currency": {
                    "name": "руб.",
                    "code": "RUB"
                    }
                 },
             "description": "Перевод со счета на счет",
             "from": "Счет 46363668439560358409",
             "to": "Счет 18889008294666828266"
            }]
    result = func.make_list_opration_object(json)
    operation = result[0]
    assert isinstance(operation, operations_cl.Operation)
