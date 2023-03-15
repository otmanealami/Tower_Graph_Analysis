import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def get_graph_info(graph):
    def average_degree(num_edges, num_nodes):
    # Cette fonction retourne le degré moyen du graphe.
        avg_degree = 0
        avg_degree = round(2 * num_edges/num_nodes)
        return avg_degree

    num_edges = graph.number_of_edges()
    num_nodes = graph.number_of_nodes()
    print("Edges number :", num_edges, "Nodes number :", num_nodes)
    avg_degree = average_degree(num_edges, num_nodes)
    print("Mean degree of the graph : {}".format(avg_degree))
    print("The mean Clustering Coefficient: {}".format(nx.average_clustering(graph)))
    
def draw_graph(graph, figsize=(12,8), title=""):
    # reproducible chart
    np.random.seed(20)
    
    # graph type checking
    graph_type = ""
    fig, ax = plt.subplots(figsize=figsize)
    for n1, n2, attribute in graph.edges.data():
        if list(attribute.keys()) != []:
            graph_type = list(attribute.keys())[0]
        break
    for _, node_attribute in bipartite_graph.nodes(data=True):
        if 'bipartite' in node_attribute.keys():
            graph_type = "bipartite"
        break
    
    if graph_type == "sign":
        edge_color_dict = {1: "green", -1: "red"}
        edge_colors = [edge_color_dict[sign] for _, _, sign in graph.edges(data="sign")]
        nx.draw(graph, with_labels=True, edge_color=edge_colors, node_size=400, font_color='white')
    elif graph_type == "weight":
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, font_color='white')
        edge_labels = dict([((n1, n2), weight) for n1, n2, weight in graph.edges(data="weight")])
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    elif graph_type == "relation":
        # create color mapping
        edge_color_dict = {0:'blue', 1:'red', 2:'green', 3:'orange', 4:'black'}
        relation_values = nx.get_edge_attributes(multigraph,'relation').values()
        unique_relations = list(set(relation_values))
        relation_color_dict = dict(zip(unique_relations , 
                                       [0] * len(unique_relations)))
        relation_index_dict = dict(zip(unique_relations , 
                                       [i for i in range(len(unique_relations))]))
        for i in range(len(unique_relations)):
            relation_color_dict[unique_relations[i]] = edge_color_dict[i]

        # draw nodes and node labels
        pos = nx.spring_layout(multigraph)
        nx.draw_networkx_nodes(multigraph, pos)
        nx.draw_networkx_labels(multigraph, pos, font_color='w')

        # draw edges with connection style of arc3 and specify the rad arguments
        for e in multigraph.edges(data="relation"):
            ax.annotate("",
                        xy=pos[e[0]], 
                        xycoords='data',
                        xytext=pos[e[1]], 
                        textcoords='data',
                        arrowprops=dict(
                            arrowstyle="-", 
                            color=relation_color_dict[e[2]],
                            shrinkA=5, shrinkB=5,
                            connectionstyle="arc3,rad=rrr".replace('rrr',
                                str(round(0.3*relation_index_dict[e[2]],2))),
                        ),
            )
        plt.axis('off')
    elif graph_type == "bipartite":
        # put L_set nodes at x=1 and R_set nodes at x=2
        L_set, R_set = bipartite.sets(graph)
        pos = dict()
        pos.update((n, (1, i)) for i, n in enumerate(L_set)) 
        pos.update((n, (2, i)) for i, n in enumerate(R_set))

        # create node color list for coloring
        node_colors = []
        for node, set_number in graph.nodes(data="bipartite"):
            if set_number == 1:
                node_colors.append("green")
            else:
                node_colors.append("blue")

        # draw the bipartite graph
        nx.draw(graph, pos=pos, with_labels=True,
                node_size=400, node_color=node_colors, font_color='white')
    else:
        nx.draw(graph, with_labels=True, font_color='white')
    plt.title(title)
    plt.show()
    
def write_edgelist(graph, filename, sep=",", data_attributes=False):
    try:
        nx.write_edgelist(graph, filename, delimiter=sep, data=data_attributes)
        print(filename, "is written sucessfully!")
    except:
        print(filename, "failed to write!")
        
def write_graph_to_pickle(graph, filename="temp.pkl"):
    import pickle
    pickle.dump(graph, open(filename, 'wb'))
    print(filename, "is save!!!")
    
def read_graph_from_pickle(filename):
    import os, pickle
    if os.path.isfile(filename):
        print("graph is loaded and returned")
        return pickle.load(open(filename, mode='rb'))
    else:
        "Input file doesn't exist!!!"
