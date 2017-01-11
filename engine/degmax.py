import networkx as nx

def get_max_deg(generated, X):
    """
    	Get the maximum node having high degree from the generated graph
		i.e. Get the hubs baby ... :D
    """
    maximum = 0
    for node in X:
        if len(list(generated.neighbors(node))) > maximum:
            start = node
            maximum = len(list(generated.neighbors(node)))

    return start
