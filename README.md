# ruuvitag_hue_temperature_indicator

## What?
A project that reads temperature from ruuvitag sensor and changes the hue light
according to the temperature.

## Installation
pip install phue
pip install python-dotenv
pip install ruuvitag_sensor

cp .env.example .env

-> edit your hue bridge ip to .env

run python main.py
