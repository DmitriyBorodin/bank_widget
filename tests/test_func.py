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