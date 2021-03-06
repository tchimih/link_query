from __future__ import division

import networkx as nx

def getStat(G):
    print " \t\t\t STATISTICS ABOUT THE GRAPH:\n"
    print " - Number of nodes: \t", len(G.nodes())
    print " - Number of edges: \t", len(G.edges())
    #print " - Number of isola: \t", len(nx.isolates(G))
    #print " - Number of trian: \t", nx.triangles(G)
    print " - Clusturing coef: \t", nx.average_clustering(G)
    print " - Transitive rato: \t", nx.transitivity(G)
    maximum = 0
    somme   = 0
    for node in list(G.nodes()):
        if G.degree(node) > maximum:
            maximum = G.degree(node)
        somme += G.degree(node)
    print " - Maximum degree: \t", maximum
    print " - Average degree: \t", somme/len(list(G.nodes()))
