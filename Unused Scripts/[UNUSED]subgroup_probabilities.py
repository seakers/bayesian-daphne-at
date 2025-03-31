# subgroup_probabilities.py
# Author: Joshua Elston
# Last Updated: 03/27/2025

# Define probabilities for the anomalies being present conditioned on the status
# of their parent group nodes. Since each anomaly is perceived to have equal
# influence over its parent group node, the presence of each anomaly under a given
# group is deemed to be equally likely in the event that that parent group node 
# is True.

# NOTE: When making changes to this file, DELETE the existing subgroup_probabilities.json
# file and rerun the script to populate updated changes


# NOTE: The dictionary defined below only includes relationships between subgroups and their
# related anomalies, as the CPT is deterministic based on the presence or absence of each anomaly
# in a given subgroup

import json

subgroup_probabilities_dict = {

    # Group 1: Carbon Dioxide Removal
    "CDRA Failure": {
         "Group 1": {
              'probabilities': {
                   True: { # Group 1 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 1 is false (i.e., no related anomalies are present)
                        'True': 0.001,
                        'False': 0.999
                   },
              },
         },
    },
    "CDRA LiOH Canister Saturation": {
         "Group 1": {
              'probabilities': {
                   True: { # Group 1 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 1 is false (i.e., no related anomalies are present)
                        'True': 0.001,
                        'False': 0.999
                   },
              },
         },
    },
    "Emergency O2 System Maintenance": {
         "Group 1": {
              'probabilities': {
                   True: { # Group 1 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 1 is false (i.e., no related anomalies are present)
                        'True': 0.001,
                        'False': 0.999
                   },
              },
         },
    },
    "Excess CO2 in Cabin": {
         "Group 1": {
              'probabilities': {
                   True: { # Group 1 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 1 is false (i.e., no related anomalies are present)
                        'True': 0.001,
                        'False': 0.999
                   },
              },
         },
    },
    "Excess Water Vapor Pressure in Cabin": {
         "Group 1": {
              'probabilities': {
                   True: { # Group 1 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 1 is false (i.e., no related anomalies are present)
                        'True': 0.001,
                        'False': 0.999
                   },
              },
         },
    },
    "RWGSR Malfunction": {
         "Group 1": {
              'probabilities': {
                   True: { # Group 1 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 1 is false (i.e., no related anomalies are present)
                        'True': 0.001,
                        'False': 0.999
                   },
              },
         },
    },
    
    # Group 2: Trace Contaminants
    "Excess Gas Leak": {
         "Group 2": {
              'probabilities': {
                   True: { # Group 2 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 2 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "TCCS Auxiliary Fan #1 Failure": {
         "Group 2": {
              'probabilities': {
                   True: { # Group 2 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 2 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "TCCS Auxiliary Fan #2 Failure": {
         "Group 2": {
              'probabilities': {
                   True: { # Group 2 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 2 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "TCCS Auxiliary Fan at Reduced Capacity": {
         "Group 2": {
              'probabilities': {
                   True: { # Group 2 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 2 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "TCCS Filter Clog": {
         "Group 2": {
              'probabilities': {
                   True: { # Group 2 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 2 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "Trace Contaminants": {
         "Group 2": {
              'probabilities': {
                   True: { # Group 2 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 2 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },

    # Group 3: Water
    "Biological Filter Saturation": {
         "Group 3": {
              'probabilities': {
                   True: { # Group 3 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 3 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "Electrolysis System Failure": {
         "Group 3": {
              'probabilities': {
                   True: { # Group 3 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 3 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "SPE System Maintenance": {
         "Group 3": {
              'probabilities': {
                   True: { # Group 3 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 3 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "WRS Failure": {
         "Group 3": {
              'probabilities': {
                   True: { # Group 3 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 3 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "WRS Maintenance": {
         "Group 3": {
              'probabilities': {
                   True: { # Group 3 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 3 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "WRS Off-nominal pH Level": {
         "Group 3": {
              'probabilities': {
                   True: { # Group 3 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 3 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },

    # Group 4: Power
    "Fuel Cell #1 and PDU Failure": {
         "Group 4": {
              'probabilities': {
                   True: { # Group 4 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 4 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },    
    "Fuel Cell #2 and PDU Failure": {
         "Group 4": {
              'probabilities': {
                   True: { # Group 4 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 4 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },  
    "Fuel Cell Degrade": {
         "Group 4": {
              'probabilities': {
                   True: { # Group 4 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 4 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },  
    "Fuel Cell Failure": {
         "Group 4": {
              'probabilities': {
                   True: { # Group 4 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 4 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },  
    "PDU 4 Failure": {
         "Group 4": {
              'probabilities': {
                   True: { # Group 4 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 4 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    }, 
    "PDU 5 Failure": {
         "Group 4": {
              'probabilities': {
                   True: { # Group 4 is true (i.e., a related anomaly is present)
                        'True': 0.167,
                        'False': 0.833  
                   },
                   False: { # Group 4 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    }, 

    # Group 5: MOXIE
    "MOXIE Antenna Failure": {
         "Group 5": {
              'probabilities': {
                   True: { # Group 5 is true (i.e., a related anomaly is present)
                        'True': 0.333,
                        'False': 0.667  
                   },
                   False: { # Group 5 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    }, 
    "MOXIE ECM Failure": {
         "Group 5": {
              'probabilities': {
                   True: { # Group 5 is true (i.e., a related anomaly is present)
                        'True': 0.333,
                        'False': 0.667  
                   },
                   False: { # Group 5 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    }, 
    "MOXIE Fan Failure": {
         "Group 5": {
              'probabilities': {
                   True: { # Group 5 is true (i.e., a related anomaly is present)
                        'True': 0.333,
                        'False': 0.667  
                   },
                   False: { # Group 5 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    }, 

    # Group 6: Main Cabin Fan
    "Main Cabin Fan Failure": {
         "Group 6": {
              'probabilities': {
                   True: { # Group 6 is true (i.e., a related anomaly is present)
                        'True': 0.5,
                        'False': 0.5  
                   },
                   False: { # Group 6 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "Reduced Main Cabin Fan #1 Capacity": {
         "Group 6": {
              'probabilities': {
                   True: { # Group 6 is true (i.e., a related anomaly is present)
                        'True': 0.5,
                        'False': 0.5  
                   },
                   False: { # Group 6 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },

    # Group 7: Decompression
    "Loss of Pressure": {
         "Group 7": {
              'probabilities': {
                   True: { # Group 7 is true (i.e., a related anomaly is present)
                        'True': 0.5,
                        'False': 0.5  
                   },
                   False: { # Group 7 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
                   },
              },
         },
    },
    "N2 Tank Burst": {
         "Group 7": {
              'probabilities': {
                   True: { # Group 7 is true (i.e., a related anomaly is present)
                        'True': 0.5,
                        'False': 0.5  
                   },
                   False: { # Group 7 is false (i.e., no related anomalies are present)
                        'True': 0.0001,
                        'False': 0.9999
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
            print("All probabilities for all anomalies under all subgroups sum to 1.0.")
    print()

# Check that the probabilities developed in the above dictionary correctly sum to one for each symptom under each anomaly
check_probabilities_sum(subgroup_probabilities_dict)

# Store subgroup probabilities dictionary as a .json file
with open("subgroup_probabilities_dict.json", "w") as file:
     json.dump(subgroup_probabilities_dict, file)