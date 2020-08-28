import bme280
from pprint import PrettyPrinter

pp = PrettyPrinter()

temperature, pressure, humidity = bme280.readBME280All()

bme = {
    'temperature': temperature,
    'pressure': pressure,
    'humidity': humidity
}

pp.pprint(bme)
