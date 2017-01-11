import matplotlib.pyplot as plt
import re 
import argparse

def draw(fin, n, m, nTest):
    """
		This function will plot:
        ------------------------
         (1) Best strategy
		 (2) Worst strategy
		 (3) Pure random strategy
		 (4) The chosen strategy
    """
    print fin
    f1 = open(fin[1], "r")
    d = (2*m)/(n*(n-1))
    best  = []
    worst = []
    rand  = []
    perso = []
    perso2= []
    cpt   = 0
    cpt2  = 0
    cpt3  = 0
    cpt4  = 0
    MAX_ITER =( n*(n-1))/2
       
    for text in f1:
        text = text.replace('\n','')
        tmp = re.split(' ', text)
        perso.append(int(tmp[0]))
    
    for i in range(0, int(max(list(perso)))):
        if (i in perso):
            cpt2 += 1
            perso2.append(cpt2)
        else:
            perso2.append(cpt2)
        if (i < m):
            best.append(cpt)
            cpt += 1
        else:
            best.append(cpt)
        if (i >= MAX_ITER - m):
            worst.append(cpt2)
            cpt2 += 1
        else:
            worst.append(0)
        rand.append(d*i)
    t = range(0, int(max(list(perso))))
    plt.plot(t, perso2)  
    plt.title(fin[1])
    plt.show()
if __name__ == '__main__':
    print " DRAW TOOL"
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fin" , nargs='+',  help="Name of the file containing the graph")
    args = parser.parse_args()
    draw(args.fin, 476, 4571 ,51)
