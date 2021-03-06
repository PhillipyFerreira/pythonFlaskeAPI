from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# Local pack
from service import service

app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin()
def hello():
    return jsonify({"message": "Welcome to BFF service"})

# List employees
@app.route("/employeesList", methods=['GET'])
@cross_origin()
def employeesList():
    """
    Expected request body
    Type: json
    body: none
    args: none

    Expected response body
    Type: json
    body:
        [{
        "employee_number": STRING,
        "name": {
            "last": STRING,
            "first": STRING,
            "middle": STRING
        },
        ...]
    """

    return jsonify(service.employeesList()), 200


# Return if employee is absent
@app.route("/isEmployeeAbsent", methods=['GET'])
@cross_origin()
def isAbsent():
    if request.method == 'GET':
        """
        Expected args
            employee_number = NUMBER
            date = YYYY-MM-DD

        Expected response body
        Type: json
        body:
            {
                "isAbsent": BOOL
            }
        """
        return jsonify(service.isEmployeeAbsent(request.args)), 200


# Status employee on specific day
@app.route("/employeeStatusOnDate", methods=['GET'])
@cross_origin()
def reasonAbsence():
    if request.method == 'GET':
        """
        Expected args
            employee_number = NUMBER
            date = YYYY-MM-DD

        Expected response body
        Type: json
        body:
            {
                "status": STRING
            }
        """
        return jsonify(service.statusEmployeeOnDate(request.args)), 200


# Group employees for Position
@app.route("/groupEmployeeByPosition", methods=['GET'])
@cross_origin()
def positionemployeeGroup():
    if request.method == 'GET':
        """
        Expected request body
        body: none
        args: none

        Expected response body
        Type: json
        body:
            [
                {
                    "position_title": STRING
                    "employees_numbers":
                    [
                        "employee_number1",
                        "employee_number2",
                        ...
                        "employee_numberN",
                    ]
                },
                ...
            ]
        """
        return jsonify(service.groupEmployeeByPosition()), 200


# Group employees for Position
@app.route("/groupEmployeeByWorkload", methods=['GET'])
@cross_origin()
def groupEmployeeByWorkload():
    if request.method == 'GET':
        """
        Expected request body
        body: none
        args: none

        Expected response body
        Type: json
        body:
            [
                {
                    "workload": STRING
                    "employees_numbers":
                    [
                        "employee_number1",
                        "employee_number2",
                        ...
                        "employee_numberN",
                    ]
                },
                ...
            ]
        """
        return jsonify(service.groupEmployeeByWorkload()), 200


# Get employee name employees by id
@app.route("/employeeName", methods=['GET'])
@cross_origin()
def getemployeeName():
    if request.method == 'GET':
        """
        Expected args
            employee_number = NUMBER

        Expected response body
        Type: json
        body:
            {
                "name": {
                    "last": STRING,
                    "first": STRING,
                    "middle": STRING
                }
            }
        """
        return jsonify(service.employeeNameById(request.args)), 200


# Get employee phone by id
@app.route("/employeePhone", methods=['GET'])
@cross_origin()
def getemployeePhone():
    if request.method == 'GET':
        """
        Expected args
            employee_number = NUMBER

        Expected response body
        Type: json
        body:
            {
                "telephone": STRING,
            }
        """
        return jsonify(service.employeePhoneById(request.args)), 200


# Get employee adress by id
@app.route("/employeeAdress", methods=['GET'])
@cross_origin()
def getemployeeAdress():
    if request.method == 'GET':
        """
        Expected args
            employee_number = NUMBER,

        Expected response body
        Type: json
        body:
            {
                "address": {
                    "description": STRING,
                    "city": STRING,
                    "state": STRING,
                    "zip": STRING
                }
            }
        """
        return jsonify(service.employeeAdressById(request.args)), 200


# Get employee position by id
@app.route("/employeePosition", methods=['GET'])
@cross_origin()
def getemployeePosition():
    if request.method == 'GET':
        """
        Expected args
            employee_number = NUMBER

        Expected response body
        Type: json
        body:
            "position": {
                "title": STRING,
                "salary": FLOAT,
                "hours": INTEGER,
                "date_of_employment": DATE
            }
        """
        return jsonify(service.employeePositionById(request.args)), 200


# List employees absences on a date
@app.route("/listAbsencesOnDate", methods=['GET'])
@cross_origin()
def getlistAbsencesOnDate():
    if request.method == 'GET':
        """
        Expected args
            date = YYYY-MM-DD

        Expected response body
        Type: json
        body:
            "employees":
                [
                    "employeeNumber1",
                    "employeeNumber2",
                    ...
                    "employeeNumberN",
                ]
        """
        return jsonify(service.listAbsencesOnDate(request.args)), 200


# List employees absences on a date
@app.route("/listEmpoyeesInRangeSalary", methods=['GET'])
@cross_origin()
def listEmpoyeesInRangeSalary():
    if request.method == 'GET':
        """
        Expected args
            initial_salary = NUMBER
            end_salary = NUMBER

        Expected response body
        Type: json
        body:
            "employees":
                [
                    "employeeNumber1",
                    "employeeNumber2",
                    ...
                    "employeeNumberN",
                ]
        """
        return jsonify(service.listEmpoyeesInRangeSalary(request.args)), 200


if __name__ == '__main__':
    app.run(port=5000)
