import PMS5003
import pprint

pp = pprint.PrettyPrinter()

particle = {
    'PM1.0': PMS5003.pm10_env,
    'PM2.5': PMS5003.pm25_env,
    'PM10.0': PMS5003.pm100_env }

pp.pprint(particle)
