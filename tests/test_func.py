from utils.func import get_executed_operations
from utils.func import sort_operations_by_date
from utils.func import format_the_operation


def test_get_executed_operations():
    operations = [
        {"state": "EXECUTED"},
        {"state": "EXECUasdTED"},
        {"state": "EXECUTED"},
        {"state": "DENIED"},
        {"statetete": "EXECUTED"},
        {"state": "executed"}
    ]
    assert get_executed_operations(operations) == [{"state": "EXECUTED"}, {"state": "EXECUTED"}]


def test_sort_operations_by_date():
    operations = [
        {"date": "2019-04-14T23:10:21.514616"},
        {"date": "2018-12-29T21:45:18.495053"},
        {"date": "2019-04-14T19:37:49.044089"},
        {"date": "2017-10-30T01:49:52.939296"}
    ]

    sorted_operations = sort_operations_by_date(operations)

    assert sorted_operations == [
        {"date": "2019-04-14T23:10:21.514616"},
        {"date": "2019-04-14T19:37:49.044089"},
        {"date": "2018-12-29T21:45:18.495053"},
        {"date": "2017-10-30T01:49:52.939296"}
    ]


def test_format_the_operation():
    operation_card_to_account = {
        "id": 871921546,
        "state": "EXECUTED",
        "date": "2019-02-14T03:09:23.006652",
        "operationAmount": {
            "amount": "47022.09",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Classic 6216537926639975",
        "to": "Счет 67667879435628279708"
    }

    assert format_the_operation(operation_card_to_account) == ("14.02.2019 Перевод организации\n"
                                                               "Visa Classic 6216 53** **** 9975 -> Счет **9708\n"
                                                               "47022.09 руб.\n")

    operation_card_to_card = {
        "id": 743278119,
        "state": "EXECUTED",
        "date": "2018-10-15T08:05:34.061711",
        "operationAmount": {
            "amount": "51203.12",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "MasterCard 1435442169918409",
        "to": "Maestro 7452400219469235"
    }

    assert format_the_operation(operation_card_to_card) == ("15.10.2018 Перевод с карты на карту\n"
                                                            "MasterCard 1435 44** **** 8409 -> Maestro 7452 40** **** "
                                                            "9235\n"
                                                            "51203.12 USD\n")

    operation_account_creation = {
        "id": 108066781,
        "state": "EXECUTED",
        "date": "2019-06-21T12:34:06.351022",
        "operationAmount": {
            "amount": "25762.92",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90817634362091276762"
    }

    assert format_the_operation(operation_account_creation) == ("21.06.2019 Открытие вклада\n"
                                                                "Счет **6762\n"
                                                                "25762.92 руб.\n")
