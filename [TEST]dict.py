# Test dictionary import

from hidden_nodes import hidden_probabilities_dict

evidence_names = []

# Iterate over all hidden nodes
for hidden_parameter, anomalies in hidden_probabilities_dict.items():
    print(hidden_parameter)
    for anomaly, data in anomalies.items():
        probabilities = data['probabilities']
        for anomaly_state, parameter_state in probabilities.items():
            print(f'Parameter state: {parameter_state}')
            for state, prob in parameter_state.items():
                print(f'Outcome: {state}, Probability: {prob}')

# testlist = list(hidden_probabilities_dict.values())
# print(testlist)

# print(evidence_names)


# testvar = '[HIDDEN] TCCS Filter Clog Component'
# testvar2 = '[HIDDEN]'

# if testvar in evidence_names:
#     print(f'Success! {testvar} is a variable within evidence_names.')
# else:
#     print(f'{testvar2} is NOT in evidence_names. :(')

# print(f'Additional evidence: {additional_evidence}' for additional_evidence in hidden_probabilities_dict.items())

# print(hidden_probabilities_dict.items()[0])

# # Add CPDs for the hidden nodes
# for hidden_parameter, anomalies in hidden_probabilities_dict.items():
#     # Generate a list of parent anomalies for the current parameter
#     anomaly_list = list(anomalies.keys())

#     # Define the states for the hidden node CPDs
#     hidden_states = ['True', 'False']

#     for anomaly, anomaly_presence in anomalies.items():

#         # print()
#         # print(f'Anomaly: {anomaly}')
#         # print(f'Anomaly presence: {anomaly_presence}')

#         hidden_values = []
#         for is_true, hidden_probabilities in anomaly_presence['probabilities'].items():
#             # print(f'Anomaly present: {is_true}')
#             # print(f'Probability: {hidden_probabilities}')

#             hidden_probs = hidden_probabilities

#             for state in hidden_states:
#                 hidden_probs = [cpt.get(state, 0) for _, cpt in anomaly_presence['probabilities'].items()]
#                 hidden_values.append(hidden_probs)

#     print(hidden_values)