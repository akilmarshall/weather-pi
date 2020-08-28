from typing import List
import strawberry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = 'sqlite:///../weather.db'
engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)


@strawberry.type
class Particle:
    pm10: List[float]
    pm100: List[float]
    pm25: List[float]


@strawberry.type
class Temperature:
    temperature_list: List[float]


@strawberry.type
class Humidity:
    humidity_list: List[float]


@strawberry.type
class Pressure:
    pressure_list: List[float]


@strawberry.type
class Query:
    temperatures: Temperature


def get_temperatures():
    session = Session()
    session.query(Temperature).all()
