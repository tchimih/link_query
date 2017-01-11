import networkx as nx

def check_edge(root, node1, node2):
    """
    	Check the existance of an edge
		For the changing part, we implemented it in the random phase :)
    """
    return (node1 in root.neighbors(node2))
