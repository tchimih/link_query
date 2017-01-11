# coding: utf-8
from __future__ import division

import re

def get_stat_eff(n ,m, t):
    """
		This function will compute the :
			
			- Worst;
			- Best;
			- Random.

		Efficiencies according the input variables, as follow:
		------------------------------------------------------
			
			(1) n:  # Nodes
			(2) m:  # Edges
			(3) t:  # Tests
    """

    density		= ((2*m)/(n*(n-1))) 	# Density that will be used in rand strategy
    max_links	= (n*(n-1))/2		    # It will be used in worst strategy
    best_eff 	= 0
    worst_eff	= 0
    rand_eff 	= 0
    shift		= 1
    cpt         = 1
    cpt_rand    = 1
    RAND_MAX_ITER = max_links - m

    for i in range(0, t+1):
        # Now we will accumulate our best, worst and rand strategies
        if ( i <= t ):
          
            # We are in the case that not all links have been discovered
            # Accumulate the best_eff
            if (i <= m): # cause we started at 0
                # Not all links had been discovered
                best_eff += i 
            else:
                # All links have been discovered
                best_eff += m

        if ( i > (RAND_MAX_ITER)):
           
            # Now we are in the case where the worst strategy operates and start
            # to accumulate, Note the the maximum number of possible links is
            # n*n-1/2 and the worst will discover the links at the
            # end.
            worst_eff += cpt
            cpt += 1
        else:
            rand_eff += shift
    # Random efficacity using linear equation
  
    rand_eff = density*0.5*t*t
    return best_eff, rand_eff, worst_eff

def get_max_eff(nTest, m):
    """
		This function will try to get the max efficiency using the best strategy
		formula and try to compute the surfaces 

		Variables:
		----------
         (1) nTest: Number of tests used !
		 (2) m    : Number of the graph links!
    """
    max_val = 0
    if (nTest <= m):
        for i in (0, nTest):
            max_val += i
        return max_val
    else:
        for i in range(0,m):
            max_val += i
        max_val += (nTest-m)*m
        return max_val

def get_min_eff(nTest, m, n):
    """
        This function will try to get the min efficiency using the worst strategy
        formula and try to compute the surfaces 

        Variables:
        ----------
         (1) nTest: Number of tests used !
         (2) m    : Number of the graph links !
         (3) n    : Number of nodes !
    """
    MAX_LINKS = (n*(n-1))/2
    min_val = 0
    if (nTest < MAX_LINKS):
        return 0
    else:
        MAX_ITER = nTest * ( ( n * ( n - 1 ) / 2 ) - m )
        for i in range(1, int(MAX_ITER)):
            min_val += i
        return min_val

def get_rand_eff(nTest, m, n):
    """
        This function will try to get the random efficiency using the pure random strategy
        formula and try to compute the surfaces 

        Variables:
        ----------
         (1) nTest: Number of tests used !
         (2) m    : Number of the graph links !
         (3) n    : Number of nodes !
    """
    rand_val = 0
    d = (2*m)/(n*(n-1))
    return int(0.5*d*pow(nTest,2))

def extract_eff(fin, n, m):
    """
		This function will compute the relative, absolute and normalized
		efficiencies from a file given as an input of the function [1]

		--------------------------------------
		[1]: fin is the file given as an input
    """
    file_in = open(fin, "r")
    
    t        = {}
    abs_eff  = 0
    rel_eff  = 0
    norm_eff = 0
    rand_eff = 0
    tmp1     = 0
    compteur = 0
    shift    = 1
    tp		 = 0
    fp		 = 0
    density = ((2*m)/(n*(n-1))) * 100

    for text in file_in:
        text = text.replace('\n','')
        tmp = re.split(' ', text)
        if int(tmp[0]) in list(t.keys()):
            # It mens that in this iteration another node has been discovered
            t[int(tmp[0])] += 1
        else:
            t[int(tmp[0])] = 1

    for i in range(0, int(max(t.keys())+1)):
        # At each step we check how many links have been discovered :)
        if i in t.keys():
            abs_eff = abs_eff + 1 + compteur
            compteur += 1
            tp += 1
            #tmp1    =  abs_eff
            #print i, " ", abs_eff
        else:
            fp += 1
            abs_eff = abs_eff + compteur
    nTest = int(max(t.keys()))
    min_val = get_min_eff(nTest, m, n)
    max_val = get_max_eff(nTest, m)
    rand_val= get_rand_eff(nTest, m, n)

    norm_eff = (abs_eff - min_val) / (max_val-min_val)
    norm_eff_rand = (rand_val - min_val) / (max_val-min_val)
    rel_eff  = (norm_eff) / (norm_eff_rand) 

    prec   = tp / (tp+fp)
    recall = tp / m
    fscore = (2*prec*recall) / (prec+recall)
    
    print "---------------------------------------------------"
    print " Statistical Informations"
    print "- Precision:\t", prec
    print "- Fscore:\t", fscore
    print "- Recall:\t", recall
    print "---------------------------------------------------"

    file_in.close()
    
    print " NOMBRE DE TEST:", nTest
    return abs_eff, rel_eff, norm_eff
