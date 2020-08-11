import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

## this route returns the converted exchange rate
@app.route("/convert", methods=["POST"])
def convert():

    print("inside convert")
    currency = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest", params={
        "access_key": "2c06bd70f654ba37a50f864947f87fa2", "symbols": currency})

    if res.status_code != 200:
        return jsonify({"success": False, "error": "There is an error"})

    data = res.json()
    print(data)

    if not (data["success"]):
        print(data["error"]["info"])
        return jsonify({"success": False, "error": data["error"]["info"]})

    if currency not in data["rates"]:
        return jsonify({"success": False, "error": "There is an error"})

    return jsonify({"success": True, "rate": data["rates"][currency]})

## this route returns the converted currecny amount
@app.route("/getamount", methods=["POST"])
def getamount():

    print("inside getamount route")

    from_cur = request.form.get("from_cur")
    to_cur = request.form.get("to_cur")
    amount = request.form.get("amount")

    res = requests.get("http://data.fixer.io/api/convert", params={
        "access_key": "2c06bd70f654ba37a50f864947f87fa2", "from": from_cur, "to": to_cur, "amount": amount})

    if res.status_code != 200:
        return jsonify({"success": False, "error": "There is an error."})

    data = res.json()
    print (data)

    if not (data["success"]):
        return jsonify({"success": False, "error": data["error"]["info"]})

    return jsonify({"success": True, "result": data["result"]})

@app.route("/historydata", methods=["POST"])
def historydata():

    print ("inside history data route")
    symbol = request.form.get("symbol")
    todate = request.form.get("todate")
    print(symbol)
    print (todate)
    api_string = "http://data.fixer.io/api/" + todate

    res = requests.get(api_string, params={
        "access_key": "2c06bd70f654ba37a50f864947f87fa2", "symbols": symbol })

    if res.status_code != 200:
        return jsonify({"success": False, "error": "There is an error."})
    print("success 1")
    data = res.json()
    print (data)

    if not data["success"]:
        return jsonify({"success": False, "error": data["error"]["info"]})
    print ("success 2")
    if symbol not in data["rates"]:
        return jsonify({"success": False, "error": "There is an error"})
    print ("success 3")
    return jsonify({"success": True, "result": data["rates"][symbol]})
