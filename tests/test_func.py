from utils.func import *


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
