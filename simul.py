import argparse
import re
import networkx as nx
import random
import time 
import sys

from engine.stat 		import 	*
from engine.exo2		import 	*
from engine.exo3		import 	*   
from engine.rand_phase 	import 	*
from engine.degmax		import 	*
from engine.complete	import 	*
from engine.analyse		import 	*
from engine.tbf			import 	*
from engine.tbfc		import	*

def type_check(v):
    if v not in ["pure-rand", "tbf", "rand", "complete", "refined", "eff-check",
"eff-spectral", "tbfc"]:
        print v
        raise argparse.ArgumentTypeError("Unknown type !")
    return v

def main():
    """
        This function will only parse the arguments to get it started :)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fin" ,help="Name of the file containing the graph")
    parser.add_argument("-o", "--fout",help="Name of the output file")
    parser.add_argument("-n", "--nbIter", help="Number of random iterations") 
    parser.add_argument("-N", "--n", type=int, help="Number of nodes")
    parser.add_argument("-M", "--m", type=int, help="Number of edges")
    parser.add_argument("-nt", "--t", type=int, help="Number of tests")
    parser.add_argument("-t", "--type", type=type_check, help="name of the support types of link prediction, the options are \
        'pure-rand', 'tbf', 'tbfc', 'rand', 'eff-check', 'eff-spectral'",
required=True)
    args = parser.parse_args()

    root      = nx.Graph() # Used as the reference graph
    sample    = nx.Graph() # Used as the tmp graph
    check     = False      # Flag to check whether it is correct
    generated = nx.Graph() # Used as the final graph to compare it with the reference
    final     = nx.Graph()


    if(args.type == "tbfc"):
        sample, root = extractGraph(args.fin, args.fout)
        print "\tStatistics about the input Graph"
        getStat(root) #Display the graph caracteristics :)
        # Launch V-Random with nbIter tests
        check, generated, treated, i = init_rand(root, sample, int(args.nbIter),
args.fout)


        if (check):
            #print " Initial random phase with ",args.nbIter," : DONE"
            print "-------------------------------------------------------------------"
            final = tbfc(root, generated, treated, i, args.fout)
            print "-------------------------------------------------------------------"
            print "\t Statistics about the output graph"
            getStat(final)

    # Launch the complete strategy 
    # Part4: Exercices 10 and 11

    if (args.type == "complete"):
        sample, root = extractGraph(args.fin, args.fout)
        print "\tStatistics about the input Graph"
        getStat(root) #Display the graph caracteristics :)
        check, generated, treated, i = init_rand(root, sample, int(args.nbIter),
args.fout)
    
     
        if (check):
            #print " Initial random phase with ",args.nbIter," : DONE"
            print "-------------------------------------------------------------------"
            final = complete_method(root, generated, treated, i, args.fout)
            print "-------------------------------------------------------------------"
            print "\t Statistics about the output graph"
            getStat(final)

    # Part4: Exercice 12 and 13
    # Launch TBF strategy with link ordering
 
    if (args.type == "tbf"):
        sample, root = extractGraph(args.fin, args.fout)
        print "\tStatistics about the input Graph"
        getStat(root) #Display the graph caracteristics :)
        # Launch V-Random with nbIter tests
        check, generated, treated, i = init_rand(root, sample, int(args.nbIter),
args.fout)


        if (check):
            #print " Initial random phase with ",args.nbIter," : DONE"
            print "-------------------------------------------------------------------"
            final = tbf(root, generated, treated, i, args.fout)
            print "-------------------------------------------------------------------"
            print "\t Statistics about the output graph"
            getStat(final)

    # Exercice N5
    if(args.type=="eff-spectral" and args.m is not None and args.n is not None and
args.t is not None):	
        print "\t Information about the graph:\n"
        best_eff, rand_eff, worst_eff = get_stat_eff(args.n, args.m, args.t)
        print " NUMBER OF TEST:", args.t
        print "- Best efficiency:\t", best_eff
        print "- Pure random effiency:\t", rand_eff
        print "- Worst efficiency:\t", worst_eff

    #Exercice N6
    if(args.type == "eff-check" and args.m is not None and args.n is not None and
args.fin is not None):
        print "\t EXECICE 6:\n"
        absolute, relative, norm = extract_eff(args.fin, args.n, args.m)
        print " FILE:", args.fin
        print "- Absolute efficiency:\t", absolute
        print "- Relative efficiency:\t", relative
        print "- Normalized efficiency:\t", norm

    # Part III: Exercices: 7, 8 & 9
    if (args.type == "rand" and args.fin is not None and args.fout is not None and
args.nbIter is not None):
        print "\t Part III: Random strategies:\n"
        sample, root = extractGraph(args.fin, "x")
        print "\t Statistics about the output graph"
        print "-------------------------------------------------------------------"
        getStat(root) #Display the graph caracteristics :)
        check, generated, treated, i = init_rand(root, sample, int(args.nbIter),
args.fout)

        if (check):
            print " Random strategy with ",args.nbIter," : DONE"
            print "-------------------------------------------------------------------"
            print "\t Statistics about the output graph"
            getStat(generated)

if __name__ == '__main__':
    print " ********************************************************************* "
    print " \t\t\t NSD PROJECT "
    print "  Developped by :\n"
    print "  - HAMMOUTENE ANIS"
    print "  - SAIDI TARIK\n"
    print " ********************************************************************* "
    main()
