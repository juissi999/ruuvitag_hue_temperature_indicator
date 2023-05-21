import os

from ruuvitag_sensor.ruuvi import RuuviTagSensor
from tinydb import TinyDB
from dotenv import load_dotenv

def handle_data(found_data):
  print('MAC ' + found_data[0])
  print(found_data[1])

if __name__ == '__main__':
  # load environment variables
  load_dotenv()

  db = TinyDB(os.getenv('DBFILE'))

  RuuviTagSensor.get_datas(handle_data)
