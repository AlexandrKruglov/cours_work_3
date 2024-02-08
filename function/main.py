from function import func
from function.config import OPERATION_JSON

operations_data = func.get_operations(OPERATION_JSON)          # чтение json файла
operation_object_list = func.make_list_opration_object(operations_data)  # создание списка объектов класса Operation
data = func.sorted_list(operation_object_list)       # список объектов класса Operation  отсортираванный по времени
data_executed = func.choos_executed_operation(data)  # список объектов класса Operation только выполненых операций
slice_operation = func.slice_last_operation(data_executed)  # срез последних 5 операций


if __name__ == '__main__':
    func.output_operation(slice_operation)
