import json
from collections import defaultdict
import jmespath

global data
with open('data.json', mode='r') as f:
    data = json.load(f)

f.close()
# for p in data:

#     r = {}
#     print('Name: ' + p['name']['first'])
#     print('Position: ' + p['position']['title'])
#     print('telephone: ' + p['telephone'])
#     print('')
#     r.update(p['name'])
#     # r.update(p['position'])
#     # r.update(p['telephone'])
#     response.update(r)
# print(response)


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
    query = {'positionList': jmespath.search('[].{ positionTitle: position.title, employee_number: employee_number}', data)}
    res = defaultdict(list)
    for v, k in query:
        res[v].append(k)
    # [{'type': k, 'items': v} for k, v in res.items()]
    return res
