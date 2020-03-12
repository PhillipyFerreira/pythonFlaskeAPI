from flask import Flask, request, jsonify
# from flask_jsonschema_validator import JSONSchemaValidator, jsonschema

# Local pack
from . import service

# import jmespath as jpath

app = Flask(__name__)
response = {}


@app.route("/")
def hello():
    return jsonify({"message": "This path don't have service"})

# Return error when json input body is invalid or incomplete
# @app.errorhandler(jsonschema.ValidationError)
# def onValidationError(e):
#     return Response("There was a validation error: " + str(e), 400)


# List employees
@app.route("/employeesList", methods=['GET'])
def employeesList():
    """
    Expected request body
    Type: json
    body: none

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
# @app.validate('employee_number', 'date')
def absent():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
                "date": DATE
            }

        Expected response body
        Type: json
        body:
            {
                "isAbsent": true / false
            }
        """
        return jsonify(service.isEmployeeAbsent(request.json))

# Status employee on specific day
@app.route("/employeeStatusOnDate", methods=['GET'])
def reasonAbsence():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
                "date": DATE
            }

        Expected response body
        Type: json
        body:
            {
                "status": STRING
            }
        """
        return jsonify(service.statusEmployeeOnDate(request.json)), 200


# Group employees for Position
@app.route("/groupEmployeeByPosition", methods=['GET'])
def positionemployeeGroup():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            none

        Expected response body
        Type: json
        body:
            {[
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
            ]}
        """
        return jsonify(service.groupEmployeeByPosition()), 200


# Get employee name employees by id
@app.route("/employeeName", methods=['GET'])
# @app.validate('employee_number')
def getemployeeName():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }
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
        return jsonify(service.employeeNameById(request.json)), 200


# Get employee phone by id
@app.route("/employeePhone", methods=['GET'])
def getemployeePhone():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }

        Expected response body
        Type: json
        body:
            {
                "telephone": STRING,
            }
        """
        return jsonify(service.employeePhoneById(request.json)), 200


# Get employee adress by id
@app.route("/employeeAdress", methods=['GET'])
def getemployeeAdress():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }

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
        return jsonify(service.employeeAdressById(request.json)), 200

# Get employee position by id
@app.route("/employeePosition", methods=['GET'])
def getemployeePosition():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }

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
        return jsonify(service.employeePositionById(request.json)), 200

# List employees absences on a date
@app.route("/listAbsencesOnDate", methods=['GET'])
def getlistAbsencesOnDate():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "date": DATE,
            }

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
        return jsonify(service.listAbsencesOnDate(request.json)), 200


if __name__ == '__main__':
    app.run(debug=True)
