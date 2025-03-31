# [UNUSED]ranges.py
# Author: Joshua Elston
# Last Edited: 12/11/2024

# Stores all measurement ranges originally captured in ranges.py that are captured in either
# Neo4j or the HSS but are not related to any anomalies (the specific rationale for each 
# measurement being stored in this script can be seen in its related note)

unused_measurement_ranges = {
    # NOTE: not related to any anomalies in Neo4j
    "DMCPS": {
        'Exceeds_UpperWarningLimit': (2, None, True, False),
        'Exceeds_UpperCautionLimit': (1.5, 2, True, False),
        'Nominal': (-1, 1.5, False, False), # Nominal: 1.43 ppm
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "Ethanol": {
        'Exceeds_UpperWarningLimit': (4, None, True, False),
        'Exceeds_UpperCautionLimit': (3.75, 4, True, False),
        'Nominal': (-1, 3.75, False, False), # Nominal: 3.45 ppm
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "Ethyl Acetate": {
        'Exceeds_UpperWarningLimit': (0.2, None, True, False),
        'Exceeds_UpperCautionLimit': (0.15, 0.2, True, False),
        'Nominal': (-1, 0.15, False, False), # Nominal: 0.03 ppm 
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "m-p Xylenes": {
        'Exceeds_UpperWarningLimit': (0.1, None, True, False),
        'Exceeds_UpperCautionLimit': (0.05, 0.1, True, False),
        'Nominal': (-1, 0.05, False, False), # Nominal: 0.0 ppm
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "OMCTS": {
        'Exceeds_UpperWarningLimit': (0.1, None, True, False),
        'Exceeds_UpperCautionLimit': (0.08, 0.1, True, False),
        'Nominal': (-1, 0.08, False, False), # Nominal: 0.04 ppm
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "o-Xylene": {
        'Exceeds_UpperWarningLimit': (0.1, None, True, False),
        'Exceeds_UpperCautionLimit': (0.05, 0.1, True, False),
        'Nominal': (-1, 0.05, False, False), # Nominal: 0.01 ppm
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 1 Bank 1": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 19.9 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 1 Bank 2": { # NOTE: In spreadsheet, listed as "PDU 1 Bank  2" <-- check if this is the same in Neo4j
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 2 Bank 1": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20.2 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 2 Bank 2": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20.1 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 3 Bank 1": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 3 Bank 2": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "PDU 4 Bank 2": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "PDU 5 Bank 2": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 6 Bank 1": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "PDU 6 Bank 2": {
        'Exceeds_UpperWarningLimit': (30, None, True, False),
        'Exceeds_UpperCautionLimit': (25, 30, True, False),
        'Nominal': (5, 25, False, False), # Nominal: 20 amps
        'Exceeds_LowerCautionLimit': (2, 5, False, True),
        'Exceeds_LowerWarningLimit': (None, 2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "ppH2O": {
        'Exceeds_UpperWarningLimit': (6.1, None, True, False),
        'Exceeds_UpperCautionLimit': (5.8, 6.1, True, False),
        'Nominal': (1.5, 5.8, False, False), # Nominal: 4.5 mmHG
        'Exceeds_LowerCautionLimit': (0.5, 1.5, False, True),
        'Exceeds_LowerWarningLimit': (None, 0.5, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j (also called Crew Quarters Humidity)
    "Quarters Humidity": {
        'Exceeds_UpperWarningLimit': (68, None, True, False),
        'Exceeds_UpperCautionLimit': (61, 68, True, False),
        'Nominal': (40, 61, False, False), # Nominal: 52.01%
        'Exceeds_LowerCautionLimit': (30, 40, False, True),
        'Exceeds_LowerWarningLimit': (None, 30, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j (also called Crew Quarters Radiation)
    "Quarters Radiation": {
        'Exceeds_UpperWarningLimit': (1.8, None, True, False),
        'Exceeds_UpperCautionLimit': (1.5, 1.8, True, False),
        'Nominal': (0.5, 1.5, False, False), # Nominal: 1.2 μGy/min
        'Exceeds_LowerCautionLimit': (-1, 0.5, False, True),
        'Exceeds_LowerWarningLimit': (None, -1, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "Radiation": { # NOTE: Only one Radiation value is stored, though it is separately measured on L1 and L2
        'Exceeds_UpperWarningLimit': (1.8, None, True, False),
        'Exceeds_UpperCautionLimit': (1.5, 1.8, True, False),
        'Nominal': (0.5, 1.5, False, False), # Nominal: 1.2 μGy/min (L1 = L2)
        'Exceeds_LowerCautionLimit': (-1, -0.5, False, True),
        'Exceeds_LowerWarningLimit': (None, -1, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "Solar Array Current": {
        'Exceeds_UpperWarningLimit': (75, None, True, False),
        'Exceeds_UpperCautionLimit': (68, 75, True, False),
        'Nominal': (55, 68, False, False), # Nominal: 60.2 Vdc
        'Exceeds_LowerCautionLimit': (48, 55, False, True),
        'Exceeds_LowerWarningLimit': (None, 48, False, True)
    },
    # NOTE: not included in Neo4j measurements
    "Solar Array Voltage": {
        'Exceeds_UpperWarningLimit': (30.2, None, True, False),
        'Exceeds_UpperCautionLimit': (29, 30.2, True, False),
        'Nominal': (27.6, 29, False, False), # Nominal: 28.6 Vdc
        'Exceeds_LowerCautionLimit': (25.2, 27.6, False, True),
        'Exceeds_LowerWarningLimit': (None, 25.2, False, True)  
    },
    # NOTE: not related to any anomalies in Neo4j
    "Toluene": {
        'Exceeds_UpperWarningLimit': (0.1, None, True, False),
        'Exceeds_UpperCautionLimit': (0.05, 0.1, True, False),
        'Nominal': (-1, 0.05, False, False), # Nominal: 0.01 ppm
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
    # NOTE: not related to any anomalies in Neo4j
    "Trimethylsilanol": {
        'Exceeds_UpperWarningLimit': (0.35, None, True, False),
        'Exceeds_UpperCautionLimit': (0.25, 0.35, True, False),
        'Nominal': (-1, 0.25, False, False), # Nominal: 0.14 ppm
        'Exceeds_LowerCautionLimit': (-2, -1, False, True),
        'Exceeds_LowerWarningLimit': (None, -2, False, True)
    },
}