import json
import operation_class
from config import OPERATION_JSON


def make_list_opration_object():
    '''
    создаем список объектов Operation из json файла
    :return: список объектов
    '''
    operations_json = OPERATION_JSON
    with open(operations_json) as file:
        operation_list = json.load(file)
        operation_object_list = []
        for item in operation_list:
            if item == {}:
                continue
            temp = operation_class.Operation(item['id'], item['date'], item['state'],
                                             item['operationAmount']['amount'],
                                             item['operationAmount']['currency']['name'],
                                             item['description'], item['to'], item.get('from', ''))
            operation_object_list.append(temp)
    return operation_object_list



def sorted_list():
    '''
  сортируем список операций по дате
    '''
    new_sort_list = sorted(make_list_opration_object(), key=lambda x: x.date)
    return new_sort_list


def choos_executed_operation(list_op):
    '''
    фильтруем список операций убираем откланенные операции
    :param list_op:поступает отсортированный список по дате
    '''
    executed_list_object = []
    for example in list_op:
        if example.check_opration_state() == True:
            executed_list_object.append(example)
        else:
            continue
    return executed_list_object

def slice_last_operation(list_op):
    '''
    отбираем последние 5 операций и переворачиваем список
    :param list_op:поступает отсортированый и отфильтрованный список
    '''
    slice_list = list_op[-5:]
    new_slice_list = slice_list[::-1]
    return new_slice_list



def add_stars_card(card):
    '''
    скрываем счет отправителя меняем цифры на звезды
    :param card:поступает счет отправителя
    '''
    num_list = []
    all_list = []
    card_1 = card.split(' ')  # разделяем название счета и его номер
    card_num = card_1[1]      # выбераем номер счета
    card_num = card_num[:6] + "******" + card_num[-4:]   # заменяем цифры на звезды
    for i in range(0, len(card_num), 4):                 # разбиваем номер по 4 знака
        temp = card_num[i:i + 4]
        num_list.append(temp)
    all_list.append(card_1[0])        # соединяем обратно название счета с номером
    all_list.extend(num_list)
    new_card = " ".join(all_list)
    return new_card


def add_star_to_chek(chek):
    '''
    скрываем счет зачисления
    '''
    new_chek = "Счет " + "**" + chek[-4:]
    return new_chek

def output_operation(list_operation):
    '''
    вывод операции в нужном формате
    '''
    for item in list_operation:
        print(f"{item.return_date()} {item.description}")
        if item.operation_from =="":
            print(f"->{add_star_to_chek(item.operation_to)}")
        elif item.operation_from != "":                 #если нет отправителя
            print(f"{add_stars_card(item.operation_from)} -> {add_star_to_chek(item.operation_to)}")
        print(f"{item.operation_amount} {item.name_amount}")
        print()

