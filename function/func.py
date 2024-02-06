import json
import operations_cl
from config import OPERATION_JSON

path_oper = OPERATION_JSON


def get_operations(oper):
    '''
    получаем список из json файла
    '''
    with open(oper) as file:
        operation_list = json.load(file)
    return operation_list


def make_list_opration_object(oper_list):
    '''
    создаем список объектов Operation
    :return: список объектов
    '''
    operation_object_list = []
    for item in oper_list:
        if item == {}:
            continue
        temp = operations_cl.Operation(item['id'], item['date'], item['state'],
                                       item['operationAmount']['amount'],
                                       item['operationAmount']['currency']['name'],
                                       item['description'], item['to'], item.get('from', ''))
        operation_object_list.append(temp)
    return operation_object_list


operation_object_list = make_list_opration_object(get_operations(path_oper))


def sorted_list():
    '''
  сортируем список операций по дате
    '''
    new_sort_list = sorted(operation_object_list, key=lambda x: x.date)
    return new_sort_list


def choos_executed_operation(list_op):
    '''
    фильтруем список операций убираем отклоненные операции
    :param list_op:поступает отсортированный список по дате
    '''
    executed_list_object = []
    for example in list_op:
        print(example)
        if example.check_operation_state() == True:
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
    card_1 = card.split(' ')  # разделяем название счета и его номер
    if card_1[0] == 'Счет':  # проверяем счет или карта если счет вызываем фун. скрыть счет
        return add_star_to_chek(card_1[1])
    else:
        new_card_temp = []
        num_list = []
        for item in card_1:
            if item.isdigit() is False:  # проверяем название карты или номер
                new_card_temp.append(item)
            else:
                card_num = item[:6] + "******" + item[-4:]  # заменяем цифры на звезды
                for i in range(0, len(card_num), 4):  # разбиваем номер по 4 знака
                    temp = card_num[i:i + 4]
                    num_list.append(temp)
    new_card_temp.extend(num_list)  # соединяем обратно название счета с номером
    new_card = " ".join(new_card_temp)
    return new_card


def add_star_to_chek(chek):
    '''
    скрываем счет зачисления
    '''
    new_chek = "Счет " + "**" + chek[-4:]
    return new_chek


def output_operation():
    '''
    вывод операции в нужном формате
    '''
    data = sorted_list()  # список отсортираванный по времени
    data_executed = choos_executed_operation(data)  # список только выполненых операций
    list_operation = slice_last_operation(data_executed)  # срез последних 5 операций
    for item in list_operation:
        print(f"{item.return_date()} {item.description}")
        if item.operation_from == "":
            print(f"->{add_star_to_chek(item.operation_to)}")
        elif item.operation_from != "":  # если нет отправителя
            print(f"{add_stars_card(item.operation_from)} -> {add_star_to_chek(item.operation_to)}")
        print(f"{item.operation_amount} {item.name_amount}")
        print()
