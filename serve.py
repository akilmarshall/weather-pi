#!/usr/bin/python3
from flask import Flask, jsonify
from flask import render_template
import json

import weatherpi.database as db


app = Flask(__name__)
application = app


@app.route("/all_temperatures", methods=['GET'])
def all_temperatures():
    data = db.get_all_temperatures() 
    return jsonify(data)


@app.route("/all_humidities", methods=['GET'])
def all_humidities():
    data = db.get_all_humidities() 
    return jsonify(data)


@app.route("/all_pressures", methods=['GET'])
def all_pressures():
    data = db.get_all_pressures() 
    return jsonify(data)


@app.route("/all_pm10", methods=['GET'])
def all_pm10():
    data = db.get_all_pm10() 
    return jsonify(data)


@app.route("/all_pm25", methods=['GET'])
def all_pm25():
    data = db.get_all_pm25() 
    return jsonify(data)


@app.route("/all_pm100", methods=['GET'])
def all_pm100():
    data = db.get_all_pm100() 
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
