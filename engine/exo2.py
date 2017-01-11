# coding: utf-8
import networkx as nx
import re

def extractGraph(fin, fout):

    """
		This function, will take as an input a graph contained in a file
		and generate a structure without information about the links

		Variables:
		----------
		
		- file_in  : the file containing the initial graph (Ex. Flicker)
		- file_out : the file containing the generated structure
		- sample   : the generated structure without the infos about the links
		-g_original: the original graph contained in file_in
    """

    file_in  = open( str(fin)  ,"r")
    file_out = open( str(fout) ,"w")

    total_nodes = []

    g_original = nx.Graph()
    sample = nx.Graph()

    for text in file_in:
        text = text.replace('\n','')
        tmp = re.split(' ', text)
        if (len(tmp) > 1):
            total_nodes.append(tmp[0])
            total_nodes.append(tmp[1])
            g_original.add_edge(tmp[0], tmp[1])
        else:
            # Presence of an isolated node !
            total_nodes.append(tmp[0])

    for node in g_original.nodes():
        file_out.write(str(node)+"\n")
        sample.add_node(node)

    file_out.close()
    file_in.close()

    print "SUCCESS : Graph cloned !\n"
    return sample, g_original

