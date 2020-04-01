import bme
import particle
from create_db import Temperature, Pressure, Humidity, PM10, PM25, PM100, DB_PATH, ENGINE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=ENGINE)


def insert_temperature(session):
    temp = Temperature(temperature=bme.bme['temperature'])
    session.add(temp)


if __name__ == '__main__':
    SESSION = Session()

    # populate_format(SESSION)  # populate the FORMAT table
    # populate_rest(SESSION)  # populate the rest of the tables

    insert_temperature(SESSION)
    SESSION.commit()
