# plot_bayesian_network.py
# Author: Joshua Elston
# Last Edited: 12/14/2024

# Plots the Bayesian Network to visualize the relationships 
# between anomalies and parameters --> called in ECLSS_Bayesian_Network.py

import matplotlib.pyplot as plt
import networkx as nx

def plot_bayesian_network(model):
    # Separate the parent (anomalies) and child (parameters) nodes
    anomalies = set()  # empty set to store parent nodes (anomalies)
    # Create empty dictionaries to store the high/low parameters for the top/bottom set of anomalies
    top_high_parameters = {}
    top_low_parameters = {}
    bottom_high_parameters = {}
    bottom_low_parameters = {}

    # Add all anomalies included in the network
    for anomaly, _ in model.edges():
        anomalies.add(anomaly) # anomalies added as parent nodes

    # Convert the anomalies set to a list for ordered processing
    anomalies = list(anomalies)

    # Split the anomalies into two subgroups for easier readibility when plotting
    mid_anomaly_idx = len(anomalies) // 2
    top_anomalies = anomalies[mid_anomaly_idx:]
    bottom_anomalies = anomalies[:mid_anomaly_idx]

    # Extract all parameters associated with each subgroup of anomalies
    for anomaly, parameter in model.edges():
        # Add parameters for the top subgroup of anomalies
        if anomaly in top_anomalies:
            if parameter.startswith("high "):
                top_high_param_name = parameter.split(' ', 1)[1] # access the variable names (needed to align high/low parameters)
                top_high_parameters[top_high_param_name] = parameter # using the variable name as a key, store the full variable name
            elif parameter.startswith("low "):
                top_low_param_name = parameter.split(' ', 1)[1] # access the variable names (needed to align high/low parameters)
                top_low_parameters[top_low_param_name] = parameter # using the variable name as a key, store the full variable name
        # Add parameters for the bottom subgroup of anomalies
        if anomaly in bottom_anomalies:
            if parameter.startswith("high "):
                bottom_high_param_name = parameter.split(' ', 1)[1] # access the variable names (needed to align high/low parameters)
                bottom_high_parameters[bottom_high_param_name] = parameter # using the variable name as a key, store the full variable name
            elif parameter.startswith("low "):
                bottom_low_param_name = parameter.split(' ', 1)[1] # access the variable names (needed to align high/low parameters)
                bottom_low_parameters[bottom_low_param_name] = parameter # using the variable name as a key, store the full variable name

    # Store unique parameter names once (allows high values to be stored above low values)
    top_base_params = sorted(set(key for key in top_high_parameters.keys() & top_low_parameters.keys()))
    bottom_base_params = sorted(set(key for key in bottom_high_parameters.keys() & bottom_low_parameters.keys()))

    print(f"Top Anomlies: {top_anomalies}")
    print(f"Top Parameters: {top_base_params}")
    print()
    print(f"Bottom Anomlies: {bottom_anomalies}")
    print(f"Bottom Parameters: {bottom_base_params}")
    print()

    # Store unique parameter names once (allows high values to be stored above low values)
    # base_params = sorted(set(high_parameters.keys()).union(low_parameters.keys()))
    # base_params = sorted(set(key for key in high_parameters.keys() & low_parameters.keys()))
    # base_params = sorted(parameters.keys())


    # # Calculate the center offset to center the high/low parameter rows w.r.t. each other
    # top_center_offset = (len(top_base_params) - len(top_anomalies)) / 2
    # bottom_center_offset = (len(bottom_base_params) - len(bottom_anomalies)) / 2

    # Create a subfunction to create plots for the two sets of anomalies and their associated parameters
    def plot_network(base_params, anomalies, high_params, low_params):
        # Calculate the center offset to center the high/low parameter rows w.r.t. each other
        center_offset = (len(base_params) - len(anomalies)) / 2

        # Manually assign positions for two distinct layers
        pos = {}

        # Position anomalies (parents) in the top layer (y = 1), centered
        for i, anomaly in enumerate(anomalies):
            pos[anomaly] = (i + center_offset, 1)

        # Position high-value parameters in the middle layer (y = 0.4), closer to the low-value layer (y = 0)
        for i, param in enumerate(high_params):
            pos[high_params[param]] = (i, 0.4) # middle layer
        for i, param in enumerate(low_params):
            pos[low_params[param]] = (i, 0) # bottom layer
    
        # Create a directed graph
        G = nx.DiGraph()
        # Add edges from the Bayesian network to the graph
        G.add_edges_from((anomaly, high_params[param]) for param in base_params for anomaly in anomalies)
        G.add_edges_from((anomaly, low_params[param]) for param in base_params for anomaly in anomalies)
            # model.edges())

        # Get a list of nodes (anomalies and parameters)
        nodes = list(G.nodes())

        # Increase the figure size dynamically based on the number of nodes
        plt.figure(figsize=(12, 6 + len(anomalies) / 4))

        if base_params == top_base_params:
            title_txt = '(pt. 1)'
        elif base_params == bottom_base_params:
            title_txt = '(pt. 2)'

        plt.title(f"ECLSS Bayesian Network {title_txt}", fontsize = 10, fontweight = 'bold')

        # Draw the nodes and edges
        nx.draw(G, pos, with_labels = False, node_size = 1125, node_color = 'lightblue', arrows = True)

        # Create a function to handle long words (>8 characters) and multi-word lines in nodes (for better readibility)
        def split_long_words_and_two_words(text):
            # Split node names (anomalies and parameters) into individual words
            words = text.split()
            lines = []
            current_line = []

            # Loop through each word in a node name
            for word in words:
                if len(word) >= 8: # if the word is 8 or more characters, it goes on its own line
                    if current_line:
                        lines.append(" ".join(current_line))
                        current_line = []
                    lines.append(word) # add the long word as a separate line
                else:
                    current_line.append(word)
                    if len(current_line) == 2: # where applicable, group two words per line
                        lines.append(" ".join(current_line))
                        current_line = []

            # Add any remaining words
            if current_line:
                lines.append(" ".join(current_line))

            return "\n".join(lines)  # Join all lines with a newline

        # Create labels for the nodes, utilizing the formatting function above
        labels = {}
        for node in nodes:
            if "high" in node or "low" in node:
                level, param = node.split(' ', 1)
                labels[node] = f"{level.capitalize()}\n{split_long_words_and_two_words(param)}"
            else:
                labels[node] = split_long_words_and_two_words(node)

        nx.draw_networkx_labels(G, pos, labels = labels, font_size = 3.75, font_weight = 'bold')

        # Add labels to distinguish the two levels (Anomalies and Parameters)
        plt.text(-1, 1, 'Anomalies', fontsize = 6, fontweight = 'bold', ha = 'right', va = 'center', color = 'black')
        plt.text(-1, 0.2, 'Parameters', fontsize = 6, fontweight = 'bold', ha = 'right', va = 'center', color = 'black')

        # Adjust axis limits for better spacing
        x_min, x_max = min(x for x, _ in pos.values()), max(x for x, _ in pos.values())
        plt.xlim(x_min - 0.6, x_max + 0.6)
        plt.ylim(-0.05, 1.05)

        plt.show()

    # Plot the two subgraphs of the Bayesian network
    plot_network(top_base_params, top_anomalies, top_high_parameters, top_low_parameters)
    plot_network(bottom_base_params, bottom_anomalies, bottom_high_parameters, bottom_low_parameters)