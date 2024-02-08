from function import func
from operations_cl import Operation

def test_slice_last_operation():
    assert func.slice_last_operation([1, 2, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]


def test_add_stars_card():
    assert func.add_stars_card("carta 12345678900987654321") == "carta 1234 56** **** 4321"
    assert func.add_stars_card("Счет 12345678900987654321") == "Счет **4321"
    assert func.add_stars_card("card card") == "card card"


def test_add_star_to_chek():
    assert  func.add_star_to_chek("счет 555555555") == "Счет **5555"


def test_return_date():
    assert Operation.return_date(Operation(179194306, '2019-05-19T12:51:49.023880', 'EXECUTED','6381.58', 'USD', 'Перевод организации','Счет 58518872592028002662', 'МИР 5211277418228469')) == "19.05.2019"


def test_check_operation_state():
    assert Operation.check_operation_state(Operation(556488059, '2019-05-17T01:50:00.166954', 'CANCELED','74604.56', 'USD', 'Перевод с карты на карту','Visa Gold 8702717057933248', 'МИР 8021883699486544')) == False


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
    assert isinstance(operation, Operation)


def test_choos_executed_operation():

    assert func.choos_executed_operation([Operation(556488059, '2019-05-17T01:50:00.166954', 'CANCELED', '74604.56', 'USD', 'Перевод с карты на карту','Visa Gold 8702717057933248', 'МИР 8021883699486544'),
                                          Operation(179194306, '2019-05-19T12:51:49.023880', 'EXECUTED', '6381.58', 'USD', 'Перевод организации','Счет 58518872592028002662', 'МИР 5211277418228469')]) == [Operation(179194306, '2019-05-19T12:51:49.023880', 'EXECUTED', '6381.58', 'USD', 'Перевод организации','Счет 58518872592028002662', 'МИР 5211277418228469')]

