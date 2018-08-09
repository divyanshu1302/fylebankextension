from bank_manager.application import app
from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from datetime import date
from operator import itemgetter
from bank_manager.models import db , BANK_COLLECTION
from bank_manager.createdata import Reading


import json, csv
from flask import request, redirect, render_template, url_for, flash, session
# from flask import Response,make_response


@app.route('/')
def index():
	 return '<h1>Welcome to Fyle Bank Manager</h1>'

# def json_response(res=None):
# 	 """
# 	 Converts dictionary/array/list to corresponding JSON structure.
# 	 :param res: dictionary/array/list or a valid json string
# 	 :return: JSON
# 	 """
# 	 json_res = jsonify(res)
# 	 return Response(json_res, mimetype="application/json")

# def jsonify(data=None):
# 	 """
# 	 Converts data to it's corresponding JSON format. If data is string then return data as it is.
# 	 If data is `None` return empty json as '{}'.
# 	 :param data: str or dictionary/list/array
# 	 :return: Jsonified version of data.
# 	 """
# 	 json_res = None
# 	 if not data:
# 			json_res = '{}'
# 	 if type(data) != str:
# 			data = {} if not data else data
# 			json_res = json.dumps(data)
# 	 return json_res

@app.route('/create_data/', methods=["GET","POST"])
def create_data():

	csvfile = open("bank_branches.csv", 'r')
	fieldnames = ("ifsc","bank_id","branch","address","city","district","state","bank_name")
	reader = csv.DictReader( csvfile, fieldnames)
	for row in reader:
		Reading(row,db=True)

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
						data = BANK_COLLECTION.find({"ifsc":ifsc_code})
						

				elif bank_name and city:
						bank_name = bank_name.strip()
						city = city.strip()
						data = BANK_COLLECTION.aggregate([
																{ "$match": { '$and': [
																		{"city" : city, "bankname" : bank_name}
																] } },
															])
				else:
						res = {
								"status": "error",
								"message": "Please provide either ifsc or both bank name and city for which need results",
								"example": "/fetchdetails?ifsc=ABHY0065006 or /fetchdetails?bankname= somename&city= somecity"
						}
						return jsonify(res)


				
				print list(data)
				res['data'] = list(data)
				res['status'] = "success"
				res['message'] = "Started streaming tweets with keywords {}".format(ifsc_code)

		except Exception as exc:
				res['status'] = "error"
				res['message'] = exc.message
				res['args'] = exc.args

		return jsonify(res)