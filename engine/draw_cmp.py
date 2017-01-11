import matplotlib.pyplot as plt
import re 
import argparse
from matplotlib.legend_handler import HandlerLine2D

def draw(fin, n, m, nTest):
    """
		This function will plot:
        ------------------------
         (1) Best strategy
		 (2) Worst strategy
		 (3) Pure random strategy
		 (4) The chosen strategy
    """
    N 		= 	0
    perso 	=	{}
    perso2	=	{}
    t		= 	{}
    line    =   []

    for i in fin:
        perso[i]  = [] 
        perso2[i] = []
        t[i]      = []      
        f = open(i, "r")
        cpt   = 0
       
        for text in f:
            text = text.replace('\n','')
            tmp = re.split(' ', text)
            perso[i].append(int(tmp[0]))
    
        for j in range(0, int(max(list(perso[i])))):
            if j in perso[i]:
                cpt += 1
                perso2[i].append(cpt)
            else:
                perso2[i].append(cpt)

        t[i] = range(0, int(max(list(perso[i]))))
        f.close()
    cpt = 0
    for i in fin:
        line = plt.plot(t[i], perso2[i])
        plt.legend(handler_map={line: HandlerLine2D(numpoints=4)})  
        cpt += 1
    plt.show()
if __name__ == '__main__':
    print " DRAW TOOL"
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fin" , nargs='+',  help="Name of the file containing the graph")
    args = parser.parse_args()
    draw(args.fin, 476, 4571 ,51)
