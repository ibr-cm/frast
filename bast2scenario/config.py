import pandas as pd

# date to evaluate (format: YYMMDD)
DATE = 210903

# hour to evaluate (format: H, range: 1-24)
# Set to 0 to evaluate a whole day
HOUR = 0

# Filename of resulting .rou.xml and .sumocfg files (without suffix)
OUT_FILE = "../ffk-bast-210903-daily/ffk-bast-" + str(DATE) + "-" + str(HOUR).zfill(2)

# Flow warmup time
FLOW_WARMUP = 400

# Additional flow parameters
# type, id, route and vehsPerHour should not be set!
FLOW_PARAMS = {
    "departLane": "best",
    "departSpeed": "max"
}

# Modify/Create values in resulting .sumocfg file
SUMOCFG_MODS = {
    "input.route-files.value": OUT_FILE[OUT_FILE.rfind('/')+1:] + ".rou.xml",
    "input.net-file.value": "../frankfurter-kreuz.net.xml",
    "input.additional-files.value": "../frankfurter-kreuz.poly.xml",
    "gui_only.gui-settings-file.value": "../frankfurter-kreuz.view.xml",
    "time.step-length.value": 0.1
}

# year to evaluate (format: YYYY)
YEAR = int("20" + str(DATE)[0:2])

# Directory of bast .csv files
DATA_DIR = "bast-data"

# Reference .rou.xml/.sumocfg file
REF_FILE = "../frankfurter-kreuz-ref"

# Counting Stations
STATIONS = pd.DataFrame({
    "short": [
        "A3O",
        "A3W",
        "A5N",
        "A5S",
        "B43O",
        "B43W"
    ],
    "stationId": [
        6872,
        6856,
        6923,
        6924,
        6772,
        6655
    ],
    "I": [
        "R1",
        "R2",
        "R2",
        "R1",
        "R2",
        "R1"
    ]
})

# Columns to use for flow generation
CSV_COLUMNS = [
    # Summe
    "KFZ",   # Alle KFZ
    "PLZ",   # Alle aus PKW-Gruppe (Pkw, Lfw, Mot)
    "Lkw",   # Alle aus LKW-Gruppe
    # PKW-Gruppe
    "Pkw",   # Pkw
    "Lfw",   # Lieferwagen
    "Mot",   # Motorräder
    "Son",   # Sonstige KFZ
    # LKW-Gruppe
    "PmA",   # Pkw mit Anhänger
    "Bus",   # Bus
    "LoA",   # LKW > 3.5t ohne Anhänger
    "Lzg",   # Lkw > 3.5t mit Anhänger (LmA) und Sattelzüge (Sat)
    "Sat",   # Sattelzüge
]

PKW_COLUMNS = ["Pkw", "Lfw", "Mot", "Son"]
LKW_COLUMNS = ["PmA", "Bus", "LoA", "LmA", "Sat"]

VEHICLE_MAPPING = {
    # PKW-Gruppe
    "Pkw" : "passenger",            # Pkw
    "Lfw" : "van",                  # Lieferwagen
    "Mot" : "motorcycle",           # Motorräder
    "Son" : "passenger_misc",       # Sonstige KFZ
    # LKW-Gruppe
    "PmA" : "passenger_trailer",    # Pkw mit Anhänger
    "Bus" : "bus",                  # Bus
    "LoA" : "truck",                # LKW > 3.5t ohne Anhänger
    "LmA" : "truck_trailer",        # Lkw > 3.5t mit Anhänger
    "Sat" : "semitrailer",          # Sattelzüge
}
