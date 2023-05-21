import os
import time

from dotenv import load_dotenv
from tinydb import TinyDB
from phue import Bridge

import lib

# load environment variables
load_dotenv()

# initialize db
db = TinyDB(os.getenv('DBFILE'))

# initialize hue bridge
b = Bridge(os.getenv('IPADDR'))

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# get lights (for now, all in hue)
lights = b.get_light_objects()

if __name__ == '__main__':
  while True:
    # get sensor data
    data = db.all()[0]
    temperature = data["data"]["temperature"]
    
    # calculate new color
    if(temperature > 0):
      color = lib.rgb_to_xy(1.0, 0, 0)
    else:
      color = lib.rgb_to_xy(0, 0, 1.0)

    # update lights
    for light in lights:
      light.xy = color 

    time.sleep(3)