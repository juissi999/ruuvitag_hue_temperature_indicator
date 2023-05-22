# ruuvitag_hue_temperature_indicator

## What?
A project that reads temperature from ruuvitag sensor and changes the hue light
according to the temperature.

## Installation & setup
Install required packages with command

`pip3 install -r requirements.txt`

Create .env file from example with command

`cp .env.example .env`

-> edit your hue bridge ip to .env

establish connection to your hue bridge

`python3 establish_hue_connection.py`

## Usage
When installation and setup complete, setup can be used by running the sensor listener program and phue actuator program.

Start the sensor listener with command
`sudo -E python3 ruuvitag_listener.py`

Start the actuator (light) with command
`python3 phue_actuator.py`