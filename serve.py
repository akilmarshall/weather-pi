from fastapi import FastAPI
import sqlalchemy as db
import weatherpi

'''
@app.route("/all_temperatures", methods=['GET'])
@app.route("/all_humidities", methods=['GET'])
@app.route("/all_pressures", methods=['GET'])
@app.route("/all_pm10", methods=['GET'])
@app.route("/all_pm25", methods=['GET'])
@app.route("/all_pm100", methods=['GET'])
'''

app = FastAPI()


# @app.get('/')
# def read_root():
#     return {'key': 'value'}

@app.get('/all_temperatures')
def get_all_temps():
    '''
    Returns all recorded temperatures as a list of (datetime, float[C]) tuples.'''
    return {'all temperatures': weatherpi.get_all_temperatures()}
