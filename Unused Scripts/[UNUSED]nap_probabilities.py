# nap_probabilities.py
# Author: Joshua Elston
# Last Updated: 03/24/2025

# Define probabilities for the different subgroups of anomalies being present
# conditioned on the presence of the 'No Anomalies Present' node. Since each
# subgroup is perceived to have equal influence over the NAP node, the presence
# of each subgroup is deemed to be equally likely in the event that NAP is True.

# NOTE: When making changes to this file, DELETE the existing nap_probabilities.json
# file and rerun the script to populate updated changes

import json

nap_probabilities_dict = {
    "Group 1": {
        "No Anomalies Present": {
            'probabilities': {
                True: { # No anomalies are present in the system
                    'True': 0.0001,
                    'False': 0.9999
                },
                False: { # At least one subgroup has an active anomaly
                    'True': 0.1428,
                    'False': 0.8572
                },
           },
        },
    },
    "Group 2": {
        "No Anomalies Present": {
            'probabilities': {
                True: { # No anomalies are present in the system
                    'True': 0.0001,
                    'False': 0.9999
                },
                False: { # At least one subgroup has an active anomaly
                    'True': 0.1428,
                    'False': 0.8572
                },
           },
        },
    },
    "Group 3": {
        "No Anomalies Present": {
            'probabilities': {
                True: { # No anomalies are present in the system
                    'True': 0.0001,
                    'False': 0.9999
                },
                False: { # At least one subgroup has an active anomaly
                    'True': 0.1428,
                    'False': 0.8572
                },
           },
        },
    },
    "Group 4": {
        "No Anomalies Present": {
            'probabilities': {
                True: { # No anomalies are present in the system
                    'True': 0.0001,
                    'False': 0.9999
                },
                False: { # At least one subgroup has an active anomaly
                    'True': 0.1428,
                    'False': 0.8572
                },
           },
        },
    },
    "Group 5": {
        "No Anomalies Present": {
            'probabilities': {
                True: { # No anomalies are present in the system
                    'True': 0.0001,
                    'False': 0.9999
                },
                False: { # At least one subgroup has an active anomaly
                    'True': 0.1428,
                    'False': 0.8572
                },
           },
        },
    },
    "Group 6": {
        "No Anomalies Present": {
            'probabilities': {
                True: { # No anomalies are present in the system
                    'True': 0.0001,
                    'False': 0.9999
                },
                False: { # At least one subgroup has an active anomaly
                    'True': 0.1428,
                    'False': 0.8572
                },
           },
        },
    },
    "Group 7": {
        "No Anomalies Present": {
            'probabilities': {
                True: { # No anomalies are present in the system
                    'True': 0.0001,
                    'False': 0.9999
                },
                False: { # At least one subgroup has an active anomaly
                    'True': 0.1428,
                    'False': 0.8572
                },
           },
        },
    },
}

# Ensure that all of the probabilities added above sum to 1.0
def check_probabilities_sum(probability_dict):
    # Initialize flag
    all_valid = True

    for parameter, anomalies in probability_dict.items():
        for anomaly, data in anomalies.items():
            # Loop over True and False entries
            for presence, states in data['probabilities'].items():
                total_probability = sum(states.values())
            if total_probability != 1.0:
                print(f"Error: Probabilities for hidden parameter '{parameter}' under anomaly '{anomaly}' ({presence}) sum to {total_probability:.2f}, not 1.0.")
                all_valid = False

    if all_valid:
            print("All probabilities for all anomaly subgroups sum to 1.0.")
    print()

# Check that the probabilities developed in the above dictionary correctly sum to one for each symptom under each anomaly
check_probabilities_sum(nap_probabilities_dict)

# Store subgroup probabilities dictionary as a .json file
with open("nap_probabilities_dict.json", "w") as file:
     json.dump(nap_probabilities_dict, file)