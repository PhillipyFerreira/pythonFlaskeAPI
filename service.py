import json
import jmespath
import itertools

from datetime import datetime
from operator import itemgetter


MAKED_DATE="%Y-%m-%d"


global data

with open('data.json', mode='r') as f:
    data = json.load(f)

f.close()


def employeesList():
    # Using map() + itemgetter()
    # Get list of particular key in list of dictionaries
    res = jmespath.search('[*].name', data)
    return res


def employeeNameById(req):
    # Get element of particular key in list of dictionaries
    res = {'name': jmespath.search('[?employee_number==\'' + req['employee_number'] + '\'].name | [0]', data)}
    return res


def employeePhoneById(req):
    # Get element of particular key in list of dictionaries
    res = {'telephone': jmespath.search('[?employee_number==\'' + req['employee_number'] + '\'].telephone | [0]', data)}
    return res


def employeeAdressById(req):
    # Get element of particular key in list of dictionaries
    res = {'address': jmespath.search('[?employee_number==\'' + req['employee_number'] + '\'].address | [0]', data)}
    return res


def employeePositionById(req):
    # Get element of particular key in list of dictionaries
    res = {'position': jmespath.search('[?employee_number==\'' + req['employee_number'] + '\'].position.title | [0]', data)}
    return res


def groupEmployeeByPosition():
    # Get element of particular key in list of dictionaries
    res = {'positionList': jmespath.search('[].{ position_title: position.title, employee_number: employee_number}', data)}
    # Temporary list to save groupBy itens
    grouped = []
    # For use groupedby the iterable needs to already be sorted on the same key function
    # Sort employee by `position_title` key --> sorted parameter: dictList, key to sort
    # Then Grouped by `position_title` in a list --> groupby parameter: dictList, key to groupBy
    for key, value in itertools.groupby(sorted(res['positionList'], key=itemgetter('position_title')), key=itemgetter('position_title')):
        tempLst = []
        for i in value:
            tempLst.append(i['employee_number'])
        grouped.append({'position_title': key, 'employees_numbers': tempLst})
    res = grouped
    return res


def listAbsencesOnDate(req):
    bla = datetime.strptime(req['date'], MAKED_DATE)
    print(bla)
    return {}