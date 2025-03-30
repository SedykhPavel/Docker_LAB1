from flask import Flask, jsonify, request
from datetime import date 

app = Flask(__name__)

class Tel:
    def __init__(self, TypeID: int, CountryCode: int, Operator: int, Number: int):
        self.TypeID = TypeID
        self.CountryCode = CountryCode
        self.Operator = Operator
        self.Number = Number

    def base(self):
        return {
            "TypeID": self.TypeID,
            "CountryCode": self.CountryCode,
            "Operator": self.Operator,
            "Number": self.Number
        }
    
class Contanct:
    def __init__(self, ID: int, Username: str, GivenName: str, FamilyName: str, Phone: Tel, Email: str, Birthday: date):
        self.ID = ID
        self.Username = Username
        self.GivenName = GivenName
        self.FamilyName = FamilyName
        self.Phone = Phone
        self.Email = Email
        self.Birthday = Birthday
    
    def base(self):
        return {
            "ID": self.ID,
            "Username": self.Username,
            "GivenName": self.GivenName,
            "FamilyName": self.FamilyName,
            "Phone": self.Phone.base(),
            "Email": self.Email,
            "Birthday": self.Birthday
        }
    
class Group:
    def __init__(self, ID: id, Title: str, Desription: str, Contacts: int):
        self.ID = ID
        self.Title = Title
        self.Desription = Desription
        self.Contacts = Contacts

    def base(self):
        return {
            "ID": self.ID,
            "Title": self.Title,
            "Description": self.Desription,
            "Contacts": self.Contacts
        }
    
@app.route("/api/v1/contact", methods=["POST"])
def create_contact():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())

@app.route("/api/v1/contact", methods=["GET"])
def get_contact():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())

@app.route("/api/v1/contact", methods=["PUT"])
def update_contact():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())

@app.route("/api/v1/contact", methods=["DELETE"])
def delete_contact():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())

@app.route("/api/v1/group", methods=["POST"])
def create_group():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())

@app.route("/api/v1/group", methods=["GET"])
def get_group():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())

@app.route("/api/v1/group", methods=["PUT"])
def update_group():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())

@app.route("/api/v1/group", methods=["DELETE"])
def delete_group():
    data = Contanct(1, "Linga", "Nguli", "Guliguli", Tel(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(data.base())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6080)
