#!/usr/bin/python3
import weatherpi
from os.path import isfile

if not isfile(weatherpi.database.DB_PATH):
    weatherpi.database.create_database()

weatherpi.database.insert_pm10()
weatherpi.database.insert_pm25()
weatherpi.database.insert_pm100()
weatherpi.database.insert_temperature()
weatherpi.database.insert_humidity()
weatherpi.database.insert_pressure()
