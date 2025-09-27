from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

BASE_URL = os.getenv("BASE_URL")

@app.route("/GetPaymentPageLink", methods=["POST"])
def GetPaymentPageLink():
    load_dotenv()
    payload = {
        "pageCode": os.getenv('pageCode'),
        "userId": os.getenv("userId"),
        "sum": os.getenv("sum"),
        "paymentNum": os.getenv("paymentNum"),
        "description": os.getenv("description"),
        "pageField[fullName]": os.getenv("pageField_fullName"),
        "pageField[phone]": os.getenv("pageField_phone"),
        "pageField[email]": os.getenv("pageField_email")
    }
    response = requests.post(BASE_URL, data=payload)
    return jsonify({"status": response.status_code,"url": response.json()["data"]["url"]})


@app.route('/WithoutRequiredField', methods=["POST"])
def WithoutRequiredField():
    load_dotenv()
    payload = {
        "pageCode": os.getenv('pageCode'),
        "sum": os.getenv("sum"),
        "paymentNum": os.getenv("paymentNum"),
        "description": os.getenv("description"),
        "pageField[fullName]": os.getenv("pageField_fullName"),
        "pageField[phone]": os.getenv("pageField_phone"),
        "pageField[email]": os.getenv("pageField_email")
    }
    response = requests.post(BASE_URL, data=payload)
    if((response.json()["status"]) == "0"):
        return jsonify(response.json()["err"]["message"])
    else:
        return jsonify(response.json())

@app.route('/WrongValue', methods=["POST"])
def WrongValue():
    load_dotenv()
    payload = {
        "pageCode": os.getenv('pageCode'),
        "userId": os.getenv("userId"),
        "sum": os.getenv("wrong_sum"),
        "paymentNum": os.getenv("paymentNum"),
        "description": os.getenv("description"),
        "pageField[fullName]": os.getenv("pageField_fullName"),
        "pageField[phone]": os.getenv("pageField_phone"),
        "pageField[email]": os.getenv("pageField_email")
    }
    response = requests.post(BASE_URL, data=payload)
    if((response.json()["status"]) == "0"):
        return jsonify(response.json()["err"]["message"])
    else:
        return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
