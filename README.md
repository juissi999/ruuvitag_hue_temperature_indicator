# ruuvitag_hue_temperature_indicator

## What?
A project that reads temperature from ruuvitag sensor and changes the hue light
according to the temperature.

## Installation
Install required packages with command
`pip install -r requirements.txt`

Create .env file from example with command
`cp .env.example .env`

-> edit your hue bridge ip to .env

establish connection to your hue bridge
`python establish_hue_connection.py`

