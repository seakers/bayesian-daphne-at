# noisy_OR.py

# Similar to the Noisy OR function, the script calculates the conditional probability tables
# for the hidden nodes conditioned on all anomalies. Noisy OR is used here as it is better
# for modeling independent causal effects from multiple parent nodes on a binary child node.
# The assumption of independence between parent anomalies may need to be re-evaluated in future,
# but is used here.

# Author: Joshua Elston
# Last Edited: 02/22/2025


# NOTE: Below commented code block automated adding probabilities between each hidden node
# and all unrelated anomalies in the network. Based on the current approach of only adding
# connections to the related anomaly, this should not be needed; still keeping here just in case

# Automate adding probabilities for all unrelated anomalies for each hidden node
# (with the intention of having 'True' nodes decrease likelihoods for that specific
# anomaly but 'False' nodes having minimal impact on the probabilities)

# # Similar to the approach taken in user_input.py, create a set of unique anomalies
# # to hasten the process of adding additional probabilities to the hidden node dictionary
# unique_anomalies = set()
# for _, anomaly in split_probability_dict.items():
#     unique_anomalies.update(anomaly.keys())

# # print(list(unique_anomalies))
# anomaly_list = list(unique_anomalies)
# # print(anomaly_list)
# anomaly_list = sorted(anomaly_list)
# # print(anomaly_list)

# for hidden_node, related_anomaly in hidden_probabilities_dict.items():
#     # print(f"Hidden component: {hidden_node}")
#     # print(f"Related Anomaly: {related_anomaly.keys()}")
#     for anomaly in anomaly_list:
#         if anomaly not in related_anomaly:
#             related_anomaly[anomaly] = {
#             'probabilities': {
#                 True: { # probabilities when the anomaly is present
#                     'True': 0.157,
#                     'False': 0.843
#                 },
#                 # NOTE: False probabilities are currently not used to try and maintain
#                 # probability distributions as they were prior to querying piece of evidence
#                 False: { # probabilities when the anomaly is absent
#                     'True': None,
#                     'False': None

#                     # 'True': 0.999,
#                     # 'False': 0.001

#                     # 'True': 0.08,
#                     # 'False': 0.92
#                 }
#             }
#         }


from itertools import product
import time

def noisy_OR(hidden_probabilities_dict):

    # Time the duration of computing the probabilities of the hidden nodes
    # conditioned on the parent anomalies
    tic = time.time()

    hidden_cpts = {}

    for hidden_node, anomalies in hidden_probabilities_dict.items():
        anomaly_list = list(anomalies.keys())
        # num_parents = len(anomaly_list)
        cpd_list = [] # create an empty list to store all individual parent-child CPDs

        for anomaly, data in anomalies.items():
            # Extract activation probabilities for each anomaly
            c_i = data['probabilities'][True]['True']

            # Create CPTs for each individual parent-child relationship
            cpd = TabularCPD()


        # Extract activation probabilities for each anomaly
        c_i = {anomaly: anomalies[anomaly]['probabilities'][True]['True'] for anomaly in anomaly_list}

        # Create a subfunction to compute the Noisy OR probabilities dynamically
        # If all parent state combinations were expanded, this would be 2^32
        # (over 2 billion), which is what caused a previous crash and computer restart
        def compute_noisy_OR(parent_state):
            active_anomalies = [anomaly_list[i] for i, state in enumerate(parent_state) if state]

            # Compute the probability that that the hidden node Y 
            # has not been produced any of the parent anomalies in X
            # Symbolically, this looks like Pr(¬y|+x_i) = Π(1 - c_i)
            prob_hidden_false = 1 # start multiplication with a value of 1

            for anomaly in active_anomalies:
                prob_hidden_false *= (1 - c_i[anomaly])

            # Compute the probability that the hidden node Y has
            # been produced by one of the parent anomalies in X
            prob_hidden_true = 1 - prob_hidden_false

            print(f"True: {prob_hidden_true}, False: {prob_hidden_false}")

            return prob_hidden_true, prob_hidden_false
        
        # Store the probability computation function instead of the full CPT
        hidden_cpts[hidden_node] = {'Parents': anomaly_list, 'CPT': compute_noisy_OR}

        # Stop timing the function run time
        toc = time.time()

        # Calculate the total run time
        total_time = toc - tic
        print(f"Function run time is {total_time}s.")

        return hidden_cpts


    #     c_i = {}
    #     for anomaly, data in anomalies.items():

    #         # Calculate the casual probability of anomaly X_i producing the
    #         # hidden node Y (i.e., being True) when it is present
    #         # Written out, this is: c_i = P(+z_i|+x_i) = 1 - q_i
    #         # Where q_i is the probability that the inhibitor I_i is active
    #         c_i[anomaly] = data['probabilities'][True]['True']

    #     # Generate all possible parent state combinations (which are all binary outcomes)
    #     parent_states = list(product([False, True], repeat = num_parents))
    #     print(f"Parent state combos: {parent_states}")

    #     # Compute the Noisy OR probabilities
    #     cpt = {}

    #     for state_tuple in parent_states:
    #         active_anomalies = [anomaly_list[i] for i, state in enumerate(state_tuple) if state]

    #         # Compute the probability that that the hidden node Y 
    #         # has not been produced any of the parent anomalies in X
    #         # Symbolically, this looks like Pr(¬y|+x_i) = Π(1 - c_i)
    #         prob_hidden_false = 1 # start multiplication with a value of 1
    #         for anomaly in active_anomalies:
    #             prob_hidden_false *= (1 - c_i[anomaly])

    #         # Compute the probability that the hidden node Y has
    #         # been produced by one of the parent anomalies in X
    #         prob_hidden_true = 1 - prob_hidden_false

    #         cpt[state_tuple] = {'True': prob_hidden_true, 'False': prob_hidden_false}

    #     hidden_cpts[hidden_node] = {'Parents': anomaly_list, 'CPT': cpt}

    # # Stop timing the function run time
    # toc = time.time()

    # # Calculate the total run time
    # total_time = toc - tic
    # print(f"Function run time is {total_time}s.")

    # return hidden_cpts
    
# Compute the Noisy OR CPTs
from hidden_nodes import hidden_probabilities_dict
hidden_cpts = noisy_OR(hidden_probabilities_dict)

for hidden_node, data in hidden_cpts.items():
    print(f"Hidden node: {hidden_node}")
    print("Parents:", data['Parents'])
    print("Conditional Probability Table:")
    for parent_state, probs in data['CPT'].items():
        print(f"{parent_state} --> {probs}")