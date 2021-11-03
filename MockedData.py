import json

def getTestData(filename):
    TEST_DATA= []

    with open(filename, 'r') as f:
        TEST_DATA=json.load(f)
    return TEST_DATA

