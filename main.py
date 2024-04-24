from utils.func import *

data_file = 'data/operations.json'

if __name__ == '__main__':

    with open(data_file, encoding='utf-8') as file:
        operations = json.load(file)

    executed_operations = get_executed_operations(operations)

    # Первый вариант функции
    print_n_last_operations(executed_operations)

    # Второй вариант функции
    # operations = sort_operations_by_date(get_executed_operations(data_file))
    # print_n_last_operations(operations)
