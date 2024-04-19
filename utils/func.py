import json
from datetime import datetime
data_file = 'utils/operations.json'


def get_executed_operations(filename):
    """
    Возвращает список словарей с операциями, имеющими статус EXECUTED
    """
    with open(data_file, encoding='utf-8') as file:
        data = json.load(file)

        result = []

        for i in data:
            if i:
                if i['state'] == 'EXECUTED':
                    result.append(i)

    return result


def sort_operations_by_date(list_of_operations):
    """
    Принимает список операций, возвращает его отсортированным по датам где первый элемент - самая последняя операция
    """
    return sorted(list_of_operations, key=lambda x: x['date'], reverse=True)


def format_the_operation(raw_operation):
    """
    Принимает опеацию в виде исходного словаря и возвращает в отформатированном виде
    """

    date = str(datetime.strptime(raw_operation['date'], '%Y-%m-%dT%H:%M:%S.%f'))[0:10]
    date = datetime.strptime(date, '%Y-%m-%d').strftime('%d.%m.%Y')

    from_ = []
    if raw_operation.get('from'):
        for string in raw_operation['from'].split():
            if string.isalpha():
                from_.append(string)
            else:
                if len(string) == 16:
                    from_.append(string[:4] + ' ' + string[5:7] + '** **** ' + string[-4:])
                else:
                    from_.append('**'+string[-4:])
        from_ = ' '.join(from_)

    to_ = []
    for string in raw_operation['to'].split():
        if string.isalpha():
            to_.append(string)
        else:
            if len(string) == 16:
                to_.append(string[:4] + ' ' + string[5:7] + '** **** ' + string[-4:])
            else:
                to_.append('**'+string[-4:])
    to_ = ' '.join(to_)

    if raw_operation.get('from'):
        second_line = f"{from_} -> {to_}"
    else:
        second_line = f"{to_}"

    return (f"{date} {raw_operation['description']}\n"
            f"{second_line}\n"
            f"{raw_operation['operationAmount']['amount']} {raw_operation['operationAmount']['currency']['name']}\n")


def print_five_last_operations():
    """
    Эта функция просто берёт и выводит 5 последних опеаций
    :return:
    """
    operations = sort_operations_by_date(get_executed_operations(data_file))
    for operation in range(5):
        print(format_the_operation(operations[operation]))


def print_n_last_operations(operations_list, n=5):
    """
    Для работы этой функции нужно передать в неё список операций и, опционально, количество опепаций которые нужно
    вывести
    :param operations_list:
    :param n:
    :return:
    """

    for operation in range(n):
        print(format_the_operation(operations_list[operation]))
