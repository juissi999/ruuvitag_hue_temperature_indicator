import os
from phue import Bridge
from dotenv import load_dotenv
import lib

# load environment variables
load_dotenv()

b = Bridge(os.getenv('IPADDR'))

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

# print(b)

# # Prints if light 1 is on or not
# b.get_light(1, 'on')

# # Set brightness of lamp 1 to max
# b.set_light(1, 'bri', 254)

# # Set brightness of lamp 2 to 50%
# b.set_light(2, 'bri', 127)

# # Turn lamp 2 on
#b.set_light(1,'on', True)

# # You can also control multiple lamps by sending a list as lamp_id
# b.set_light( [1,2], 'on', True)

# # Get the name of a lamp
# b.get_light(1, 'name')

# # You can also use light names instead of the id
# b.get_light('Kitchen')
# b.set_light('Kitchen', 'bri', 254)

# # Also works with lists
# b.set_light(['Bathroom', 'Garage'], 'on', False)

# # The set_light method can also take a dictionary as the second argument to do more fancy stuff
# # This will turn light 1 on with a transition time of 30 seconds
# command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
# b.set_light(1, command)


# # RGB colors to XY  
defaults = lib.rgb_to_xy(255.0/256, 166.0/256, 87.0/256)
purple = lib.rgb_to_xy(1.0, 0.28627, 0.95686)

lights = b.get_light_objects()

finished = False

while not finished:
  print("Add command (q:quit | d:default color | p:purple)")
  
  variable = raw_input()

  if (variable=="q"):
    finished = True
  elif (variable=="d"):
    for light in lights:
      light.xy = defaults 
  elif (variable=="p"):
    for light in lights:
      # y might be used as brightness value, however, dark colors will turn the lights off
      #brightness = int(xy[1]*255)
      light.xy = purple

