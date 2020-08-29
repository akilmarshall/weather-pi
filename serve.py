from flask import Flask, jsonify
from flask import render_template
import json

import weatherpi.database as db


app = Flask(__name__)



@app.route("/all_temperatures", methods=['GET'])
def all_temperatures():
    data = db.get_all_temperatures() 
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
