import pytest
from function import func
from function import operation_class
import main


class For_test:
    def __init__(self, first, second):
        self.first = first
        self.second =second
    def check_operation_state(self):
        if self.first == 1:
            return True
        else:
            return False

test_class = For_test(1,2)
test_class1 = For_test(3,4)


def test_main():
    assert main.data != func.sorted_list()

def test_slice_last_operation():
    assert func.slice_last_operation([1, 2, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]

def test_make_list_opration_object():
    json = [{}]
    json_1 = [{
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
    assert func.make_list_opration_object(json) == []
    assert func.make_list_opration_object(json_1) != [operation_class.Operation(957763565, "2019-01-05T00:52:30.108534",
                                                                                  "EXECUTED", "87941.37", "руб.", "Перевод со счета на счет",
                                                                                "Счет 18889008294666828266", "Счет 46363668439560358409")]

def test_choos_executed_operation():
     assert func.choos_executed_operation([test_class, test_class1]) == [test_class]
     assert func.choos_executed_operation([test_class1]) == []
     assert func.choos_executed_operation([]) == []