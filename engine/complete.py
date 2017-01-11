import networkx as nx
import random

from sets   import  Set
from exo3	import	*
from degmax	import *

def complete_method(root, generated, treated, n, fout):
    """
    	This strategy will launch after the random graph generation
    """
    # Get :wdict from the generated
    f = open(fout, "a")

    m = len(list(root.edges()))					# The initial number of nodes
    m_bis = len(list(generated.edges())) + 1    # The generated number of nodes from V-rand

    treated_edges = treated						# Retrieve the treated nodes from the V-rand
    nodes = list(root.nodes())
    X = list(root.nodes())

    start = get_max_deg(generated, X)			# Get the node with the max degree
    i = n
    #threshold =0.1 *  m							# Set the threshold
    threshold = 10000
    
    print " Launching the Complete strategy ..."

    #while(m_bis <= threshold):
    while (i <= threshold):
        for node in list(generated.nodes()):
            if ((start != node) and Set([start, node]) not in treated_edges and
Set([node, start]) not in treated_edges and (node not in generated.neighbors(start))):
                if(root.has_edge(start, node)):
                    m_bis += 1
                    if (i >= threshold):
                        break;
                    treated_edges.append(Set([start, node]))
                    treated_edges.append(Set([node, start]))
                    generated.add_edge(start, node)
                    f.write(str(i) + " " + str(start) + " " + str(node) + "\n")
                    print i,"\t",start,"\t",node, "\t", i
                else:
                    treated_edges.append(Set([start,node]))
                    treated_edges.append(Set([node,start]))
                i += 1
        # Remove the treated node from X !
        if start in generated.nodes():
                    X.remove(start)
        start = get_max_deg(generated, X)
       

    f.close()
    print " Complete strategy: DONE"
    return generated
