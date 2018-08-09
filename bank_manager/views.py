import csv
import json

from flask import abort, jsonify, request

from bank_manager.application import app
from bank_manager.createdata import Reading
from bank_manager.models import BANK_COLLECTION, db


@app.route('/')
def index():
    return '<h1>Welcome to Fyle Bank Manager</h1>'


@app.route('/create_data/', methods=["GET", "POST"])
def create_data():

    csvfile = open("bank_branches.csv", 'r')
    fieldnames = ("ifsc", "bank_id", "branch", "address", "city", "district", "state", "bank_name")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        Reading(row, db=True)

    return jsonify({"status": "done"})


@app.route('/fetchdetails')
def fetchdetails():
        res = dict()
        ifsc_code = request.args.get('ifsc')
        bank_name = request.args.get('bankname')
        city = request.args.get('city')

        try:
                if ifsc_code:
                        ifsc_code = ifsc_code.strip()
                        data = list(BANK_COLLECTION.find({"ifsc": ifsc_code}, {"_id": 0}))

                elif bank_name and city:
                        bank_name = bank_name.strip()
                        city = city.strip()
                        data = list(BANK_COLLECTION.find({"city": city, "bank_name": bank_name}, {"_id": 0}))

                else:
                        res = {
                                "status": "error",
                                "message": "Please provide either ifsc or both bank name and city for which need results",
                                "example": "/fetchdetails?ifsc=ABHY0065006 or /fetchdetails?bankname= somename&city= somecity"
                        }
                        return jsonify(res)

                res['data'] = data
                res['status'] = "success"
                res['message'] = "Suceesfully Extracted"

        except Exception as exc:
                res['status'] = "error"
                res['message'] = exc.message
                res['args'] = exc.args

        return jsonify(res)
