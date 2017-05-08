import numpy as np
import os
import re
import string
import textwrap
import sys

#run the program with the pair of sequences
#this method creates the score matrix and calculates the optimal 
#score subject to the constraint D
def GO(seq1, seq2):
    
    num_rows = len(seq1) + 1
    num_cols = len(seq2) + 1
    
    #find the maximum score in the matrix. Must be less than D
    maxscore = CSM(num_rows, num_cols)


    #traceback to find the optimal path
    if maxscore == -1:
        print("Too many mismatches and indels according to constraint, "
            "Alignment not possible")
    else:
        print("Alignment is possible according to constraint")
    
    
    

#create the scoring matrix here
def CSM(rows, cols):

    Matrix = np.zeros(shape=(rows, cols), dtype=np.int)
    
    maxscore = 0
    maxpos = None
    for i in range(D, rows-D):
        for j in range(i-D, i+D):
            score = calc_score(Matrix, i, j)
            if score > maxscore:
                maxscore = score
                maxpos = (i, j)
            if score == -1:
                return -1

            Matrix[i][j] = score

    return maxscore


#compute the score of each 
def calc_score(Matrix, i, j):

    sim = m if seq1[i-1] == seq2[j-1] else s

    S1 = Matrix[i-1][j-1] + sim
    S2 = Matrix[i-1][j] + d
    S3 = Matrix[i][j-1] + d
    
    #print(S1, S2, S3)
    if S1 > D and S2 > D and S3 > D:#if all 3 
        return -1 
    elif S1 > D and S2 > D:
        return S3
    elif S1 > D and S3 > D:
        return S2
    elif S2 > D and S3 > D:
        return S1
    elif S3 > D:
        return max(S1, S2)
    elif S2 > D:
        return max(S1, S3)
    elif S1 > D:
        return max(S2, S3)
    else: 
        return max(S1, S2, S3)




f = open(sys.argv[1], 'r')
#P1 = open("Param1data.txt", 'w')
pline = f.readline()

m = int(sys.argv[2])
s = int(sys.argv[3])
d = int(sys.argv[4])
D = int(sys.argv[5])
a = False
total_score = 0
seq1 = seq2 = None
#go through the sequence file
i = 1
while pline != "":
    
    
    if seq1 != None and seq2 != None:
        print("running sequence pair ", i) 
        i+=1
        GO(seq1, seq2)
        seq1 = None
        seq2 = None
        total_score = 0
        continue
    if '>' in pline and seq1 == None :
        pline = f.readline()
        seq1 = pline.rstrip('\n')
        continue
    elif '>' in pline and seq2 == None:
        pline = f.readline()
        seq2 = pline.rstrip('\n')
        continue

    pline = f.readline()

#print("DONEDONEDONEDONEDONEDONEDONEDONE!!!!!!!!!")

