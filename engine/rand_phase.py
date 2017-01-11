import networkx as nx
import random

from exo3 import *
from sets import  Set

def init_rand(root, generated_graph, nbIter, fout):
    """
    	Check if a link exists and if it does, append it to the file FILE_RES
		in the specified format (t, n1, n2):

		Variables:
		---------
			- treated_items	: An array containing the links that have been
			  discovered within this random phase*
			- generated_graph: The generated structure within the random phase
		----------------------------------------------------------------------
		(*) : 	We consider this approach as a random phase, we know that we
				anticipated the treatments.
    """
        
    treated_items = []
    #generated_graph = nx.Graph()
    nTest = 0

    fout = open(fout, "w")
    nodes = list(root.nodes())
    while True:

        node1 = random.choice(nodes)
        node2 = random.choice(nodes)

        while(node1 == node2):
           node1 = random.choice(nodes)
           node2 = random.choice(nodes)

        if(root.has_edge(node1, node2) and not
generated_graph.has_edge(node1,node2) and Set([node1, node2]) not in treated_items
and Set([node2, node1]) not in treated_items):
            nTest += 1
            if (nTest > nbIter):
                break;
            generated_graph.add_edge(node1,node2)
            fout.write(str(nTest) + " " + str(node1) + " " + str(node2) + "\n")
            #print nTest, "\t", node1,"\t", node2

            # Test within the neighboors the existance of edge (node1, w) for w in
            # N(node2)
            for w in generated_graph.neighbors(node2):	
                if((root.has_edge(node1, w)) and not
generated_graph.has_edge(node1,w) and Set([node1, w]) not in treated_items
and Set([w, node1]) not in treated_items):
                    nTest += 1
                    if (nTest > nbIter):
                        break;
                    fout.write(str(nTest) + " " + str(node1) + " " + str(w) + "\n")
                    generated_graph.add_edge(node1, w)
                    #print nTest, "\t", node1,"\t", node2
                else:
                    nTest += 1
                    if (nTest > nbIter):
                        break;
                    treated_items.append(Set([node1,w]))
                    treated_items.append(Set([w,node1]))
            for w in generated_graph.neighbors(node1): 
                if(root.has_edge(node2, w)and not
generated_graph.has_edge(w,node2) and Set([w, node2]) not in treated_items
and Set([node2, w]) not in treated_items):
                    nTest += 1
                    if (nTest > nbIter):
                        break;
                    #print nTest, "\t", node1,"\t", node2
                    generated_graph.add_edge(w ,node2)
                    fout.write(str(nTest) + " " + str(node2) + " " + str(w) +
"\n")
                else:
                    nTest += 1
                    if (nTest > nbIter):
                        break;
                    treated_items.append(Set([node2, w]))
                    treated_items.append(Set([w, node2]))
        else:
            nTest += 1
            if (nTest > nbIter):
                break;
            # We save the items that have already been treated and which doesn't
            # have links
            treated_items.append(Set([node1,node2]))
            treated_items.append(Set([node2,node1]))

    fout.close()
    print " SUCCESS: Random phase DONE !\n" 
    #print treated_items
    nTest -= 1
    return True, generated_graph, treated_items, nTest
