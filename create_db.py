from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Integer, Float, Column, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

DB_PATH = 'mysql+pymysql://akil:junglepass@notserver/weather'
ENGINE = create_engine(DB_PATH, echo=True)
BASE = declarative_base()

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


if __name__ == '__main__':
    BASE.metadata.create_all(ENGINE)
