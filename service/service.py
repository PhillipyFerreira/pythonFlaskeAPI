import json
import jmespath
import itertools

from datetime import datetime
from operator import itemgetter


MAKED_DATE = "%Y-%m-%d"


global data

with open('data/employees.json', mode='r') as f:
    data = json.load(f)

f.close()


def employeesList():
    # Get list of particular key in list of dictionaries
    res = jmespath.search('[*].{ employee_number: employee_number, name: name}', data)
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
    # Temporary dict to save groupBy itens
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
    # Get all employees absences on specific date
    query = jmespath.search('[].{ employee_number: employee_number, period_absences_date: absences[].' +
                            '{initial: period.initial_date, end: period.end_date}}', data)
    res = {}
    res['employees_numbers'] = []
    for employee in query:
        for period in employee['period_absences_date']:
            if (datetime.strptime(req['date'], MAKED_DATE) >= datetime.strptime(period['initial'], MAKED_DATE) and
                    datetime.strptime(req['date'], MAKED_DATE) <= datetime.strptime(period['end'], MAKED_DATE)):
                res['employees_numbers'].append(employee['employee_number'])
    return res


def statusEmployeeOnDate(req):
    # Get employee working status on specific date
    query = jmespath.search('[?employee_number==\'' + req['employee_number'] + '\'].absences | [0] ', data)
    res = {}
    for absence in query:
        print(absence['period'])
        if (datetime.strptime(req['date'], MAKED_DATE) >= datetime.strptime(absence['period']['initial_date'], MAKED_DATE) and
                datetime.strptime(req['date'], MAKED_DATE) <= datetime.strptime(absence['period']['end_date'], MAKED_DATE)):
            res['status'] = absence['type']
            return res

    if datetime.strptime(req['date'], MAKED_DATE) > datetime.today():
        res['status'] = 'absence no previst'
        return res

    res['status'] = 'worked'
    return res


def isEmployeeAbsent(req):
    # Get if employee is absent
    query = jmespath.search('[?employee_number==\'' + req['employee_number'] + '\'].absences | [0] ', data)
    res = {}
    for absence in query:
        if (datetime.strptime(req['date'], MAKED_DATE) >= datetime.strptime(absence['period']['initial_date'], MAKED_DATE) and
                datetime.strptime(req['date'], MAKED_DATE) <= datetime.strptime(absence['period']['end_date'], MAKED_DATE)):
            res['isAbsent'] = True
            return res

    res['isAbsent'] = False
    return res


def listEmpoyeesInRangeSalary(req):
    # Get employee working status on specific date
    query = jmespath.search('[].{ employee_number: employee_number, salary: position.salary }', data)
    res = {}
    res['employees_numbers'] = []
    for employee in query:
        if (float(req['initial_salary']) <= employee['salary'] and
                float(req['end_salary']) >= employee['salary']):
            res['employees_numbers'].append(employee['employee_number'])
    return res
