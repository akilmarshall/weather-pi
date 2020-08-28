from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Integer, Float, Column, DateTime, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from . import bme280
from . import PMS5003

DB_PATH = 'sqlite:////home/pi/weather-pi/weather.db'
ENGINE = create_engine(DB_PATH, echo=True)
BASE = declarative_base()
Session = sessionmaker(bind=ENGINE)
session = Session()


class Meta(BASE):
    __tablename__ = 'META'

    info_id = Column(Integer, primary_key=True)
    table_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)


class Temperature(BASE):
    __tablename__ = 'TEMPERATURE'

    date = Column(DateTime(), default=datetime.now, primary_key=True)
    temperature = Column(Float, nullable=False)


class Humidity(BASE):
    __tablename__ = 'HUMIDITY'

    date = Column(DateTime(), default=datetime.now, primary_key=True)
    humidity = Column(Float, nullable=False)


class Pressure(BASE):
    __tablename__ = 'PRESSURE'

    date = Column(DateTime(), default=datetime.now, primary_key=True)
    pressure = Column(Float, nullable=False)


class PM10(BASE):
    __tablename__ = 'PM10'

    date = Column(DateTime(), default=datetime.now, primary_key=True)
    pm10 = Column(Integer, nullable=False)


class PM25(BASE):
    __tablename__ = 'PM25'

    date = Column(DateTime(), default=datetime.now, primary_key=True)
    pm25 = Column(Integer, nullable=False)


class PM100(BASE):
    __tablename__ = 'PM100'

    date = Column(DateTime(), default=datetime.now, primary_key=True)
    pm100 = Column(Integer, nullable=False)


def create_database():
    BASE.metadata.create_all(ENGINE)


def insert_temperature():
    t, _, _ = bme280.readBME280All()
    temp = Temperature(temperature=t)
    session.add(temp)
    session.commit()


def insert_humidity():
    _, _, h = bme280.readBME280All()
    humidity = Humidity(humidity=h)
    session.add(humidity)
    session.commit()


def insert_pressure():
    _, p, _ = bme280.readBME280All()
    pressure = Pressure(pressure=p)
    session.add(pressure)
    session.commit()


def insert_pm10():
    particle_count = PMS5003.pm10_env if PMS5003.pm10_env is not None else -1
    pm10 = PM10(pm10=particle_count)
    session.add(pm10)
    session.commit()


def insert_pm25():
    particle_count = PMS5003.pm25_env if PMS5003.pm25_env is not None else -1
    pm25 = PM25(pm25=particle_count)
    session.add(pm25)
    session.commit()


def insert_pm100():
    particle_count = PMS5003.pm100_env if PMS5003.pm100_env is not None else -1
    pm100 = PM100(pm100=particle_count)
    session.add(pm100)
    session.commit()


def get_all_temperatures():
    result = session.query(Temperature).all()
    print(type(result))
    print(result)
    print(type(result))
