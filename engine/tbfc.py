import networkx as nx
import random

from sets           import  Set
from engine.tbf     import  *
from engine.degmax  import  *

def tbf_step(root, generated, treated, n, fout):
    """
                This function implements the TBF strategy for an input graph
    """
    treated_edges = treated

    f = open(fout,"a")
    links = link_order(generated, 1)
    m_bis = len(list(generated.edges())) + 1
    m     = len(list(root.edges()))
    nTest = n
    #threshold = m*0.1
    threshold = 10000

    for j in links:
        #if (m_bis >= threshold):
        if (nTest > threshold):
            break

        node1 = links[j][1]
        node2 = links[j][2]
        if (Set([node1,node2]) not in treated_edges and Set([node2,node1]) not in treated_edges):
            # The set never been treated
            # check the existance of the link
            if (root.has_edge(node1, node2)):
                generated.add_edge(node1, node2)
                # We don't update, still we carry on with the tbf until links is empty
                #links = link_order(generated)
                f.write(str(nTest) + " " + str(node1) + " " + str(node2) + "\n")
                #print node1, "\t", node2, "\t", nTest
                m_bis += 1
                if (m_bis >= threshold):
                    break
            nTest += 1
            treated_edges.append(Set([node1,node2]))
            treated_edges.append(Set([node2,node1]))
    f.close()
    print m_bis
    return generated, treated_edges, nTest

def complete_method_step(root, generated, treated, n, fout):
    """
        This strategy will launch after the random graph generation
    """

    # Get :wdict from the generated
    f = open(fout, "a")
    final = nx.Graph()

    m = len(list(root.edges()))
    m_bis = len(list(generated.edges())) + 1

    treated_edges = treated
    nodes = list(root.nodes())
    X = list(root.nodes())

    start = get_max_deg(generated, X)
    i = n
    #threshold = 0.1*m
    threshold = 10000
 
    #while(m_bis <= threshold):
    while (i <= threshold):
            #Check if the graph generateed has diffrent linkes numbers than the root
        #print m, "\t",m_bis,"\t",start
        for node in list(generated.nodes()):
            if ((start != node) and Set([start, node]) not in treated_edges and
Set([node, start]) not in treated_edges and (node not in generated.neighbors(start))):
                if(root.has_edge(start, node)):
                    m_bis += 1
                    #if (m_bis >= threshold):
                    if (i > threshold):
                        break;
                    treated_edges.append(Set([start, node]))
                    treated_edges.append(Set([node, start]))
                    generated.add_edge(start, node)
                    f.write(str(i) + " " + str(start) + " " + str(node) + "\n")
                    print i,"\t",start,"\t",node,"\t", m_bis
                else:
                    treated_edges.append(Set([start,node]))
                    treated_edges.append(Set([node,start]))
                i += 1
        # Remove the treated node from X !
        if start in generated.nodes():
                    X.remove(start)
        start = get_max_deg(generated, X)
       #print start
    print "End complete loop", i
    f.close()
    return generated

def tbfc(root, generated, treated, i, fout):
    """
    This function will try to use the TBF and Complete strategy combined in order
    to have an efficient link query prediction
    """
    print " Starting TBF strategy "
    gen, treated_edges, n = tbf_step(root, generated, treated, i, fout)
    print " TBF strategy: completed !"
    print " Starting complete strategy"
    final = complete_method_step(root, gen, treated_edges, n, fout)
    print " TBFC strategy: DONE"
    return final
