import networkx as nx
import random

from sets   import  Set

def link_order(G, n):
    """
		This function will try to sort the links according to the order of their
		nodes

		Variables:
		---------
		
			(1) G: the generated graph from a previous strategy (V-rand in our case)
			(2) n: the degree of the node, we make it variable in order to test the efficiency, the best is
				   n = 3
    """
    tmp_g      = {}
    tmp_nodes  = []
    order_link = {}
    links      = {}
    tmp        = 0
    k		   = 0

    for node in G.nodes():
        tmp_g[node] = len(list(G.neighbors(node)))

    # Order the generated dictionnary containing node and its degree

    for node1 in tmp_g:
        for node2 in tmp_g:
            if (node1 != node2 and node2 not in tmp_nodes):
                # compute the degree sum of the link
                tmp = int(tmp_g[node1]) + int(tmp_g[node2])
                if (tmp > n):
                    order_link[k] = []
                    order_link[k].append(tmp)
                    order_link[k].append(node1)
                    order_link[k].append(node2)
                    k += 1
        tmp_nodes.append(node1)

    # Order the dict
    k= 0 
    for key, value in sorted(order_link.items(), key=lambda e: e[1][0], reverse=True):
        links[k] = value
        k += 1
    return links

def tbf(root, generated, treated, n, fout):
    """
		This function implements the TBF strategy for an input graph

		Variables:
		---------
			(1) root: The original graph (reference one)
			(2) generated: The generated graph from a previous step
			(3) treated_items: the treated items from the previous step in order not to treat them, we need	
							   to hash them in order to fast our algorithm !
			(4) n : the number of tests from the previous step !
			(5) fout: the file where to store the link prediction as follows:
						(#test Node1 Node2)
    """
    print "Launching TBF strategy ..."

    treated_edges = treated
    f = open(fout,"a")

    links = link_order(generated, 1)
    m_bis = len(list(generated.edges())) + 1
    m     = len(list(root.edges()))
    nTest = n

    #threshold = int(m * 0.01) 	# The limit
    threshold = 20000

    #while ( m_bis <= threshold ):
    while (nTest <= threshold):
        for j in links:
            if nTest > threshold:
                break
            node1 = links[j][1]
            node2 = links[j][2]
            if (not generated.has_edge(node1, node2) and Set([node1,node2]) not in treated_edges and Set([node2,node1]) not in treated_edges):
                if(root.has_edge(node1, node2)):
                    generated.add_edge(node1, node2)
                    links = link_order(generated, 1)
                    f.write(str(nTest) + " " + str(node1) + " " + str(node2) + "\n")
                    print node1, "\t", node2, "\t", nTest
                    m_bis += 1
                    if threshold <= nTest:
                    #if (threshold <= m_bis):
                        break
                nTest += 1
                treated_edges.append(Set([node1,node2]))
                treated_edges.append(Set([node2,node1]))

    f.close()
    print "TBF strategy: DONE"
    return generated
