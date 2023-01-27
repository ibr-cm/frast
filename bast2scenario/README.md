# bast2scenario
Tool to create flows for the Frankfurter Kreuz SUMO Traffic (FraST) scenario.

## Usage
To create your own flows, you need to download the hourly statistics data of all six counting stations from the [bast (Federal Highway Research Institute) website](https://www.bast.de/DE/Verkehrstechnik/Fachthemen/v2-verkehrszaehlung/zaehl_node.html).
The desired counting station IDs are: 6655, 6772, 6856, 6872, 6923 and 6924.
The downloaded csv-files must be placed in the `bast-data/` directory.
Further configuration can be done in the config-file: `config.py`.
There you need to specify the date and hour to evaluate, as well as the filename of the resulting scenario.
When setting `HOUR=0`, a 24h scenario will be created.
Otherwise, a value between 1 and 24 is expected, which denotes the 1st to 24th hour of the day (e.g. 1 denotes 00:00 - 00:59).
The resulting scenario will then have a length of one hour.
Optionally, a warmup time, additional flow parameters or modification to the sumocfg-file can be specified.
In case of a 24h scenario, the warmup time will only be added to the first hour.
Executing `bast2scenario.py` will then create a scenario for the given date and time.
