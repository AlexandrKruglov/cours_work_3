import json
import operation_class
from config import OPERATION_JSON


def make_list_opration_object():
    operations_json = OPERATION_JSON
    with open(operations_json) as file:
        operation_list = json.load(file)
        operation_object_list = []
        for item in operation_list:
            if item == {}:
                break
            temp = operation_class.Operation(item['id'], item['date'], item['state'], item['operationAmount']['amount'], item['description'], item['to'])#, item['name'], item['description'], item['to'], item[
            operation_object_list.append(temp)
    return operation_object_list


n_list = sorted(make_list_opration_object(), key=lambda x: x.date)


oo_list = n_list[-5:]
for it in oo_list:
    print(it)
