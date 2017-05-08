import numpy as np
import os
import re
import string
import textwrap
import sys



def GO(seq1, seq2, a):
    
    num_rows = len(seq1) + 1
    num_cols = len(seq2) + 1

    #initialize the scoring matrix
    Matrix, start, maxscore = CSM(num_rows, num_cols)

    #traceback to find the optimal path
    ali_seq1, ali_seq2 = traceback(Matrix, start)
    assert len(ali_seq1) == len(ali_seq2), 'aligned strings are not the same size'
    
    if a == True:
        print(ali_seq1)
        print(ali_seq2)
        return
    
    print("Optimal sequence score is ", maxscore)
    print("Optimal aligement sequence length is ", len(ali_seq1))
    datapt = str(len(ali_seq1)) + '\n'
    P1.write(datapt)

#create the scoring matrix here
def CSM(rows, cols):

    Matrix = np.zeros(shape=(rows, cols), dtype=np.int)
    
    maxscore = 0
    maxpos = None
    
    for i in range(1, rows):
        for j in range(1, cols):
            score = calc_score(Matrix, i, j)
            if score > maxscore:
                maxscore = score
                maxpos = (i, j)

            Matrix[i][j] = score

    return Matrix, maxpos, maxscore


def calc_score(Matrix, i, j):

    sim = m if seq1[i-1] == seq2[j-1] else s

    S1 = Matrix[i-1][j-1] + sim
    S2 = Matrix[i-1][j] + d
    S3 = Matrix[i][j-1] + d

    return max(0, S1, S2, S3)

#trace the best alignment from bottom left to top right of the score matrix
def traceback(Matrix, start):

    END, DIA, UP, LEFT = range(4)
    aligned_seq1 = []
    aligned_seq2 = []
    x, y = start
    move = next(Matrix, x, y)

    while move != END:
        if move == DIA:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append(seq2[y - 1])
            x -= 1
            y -= 1
        elif move == UP:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append('-')
            x -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[y - 1])
            y -= 1

        move = next(Matrix, x, y)

    aligned_seq1.append(seq1[x - 1])
    aligned_seq2.append(seq2[y - 1])

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))


#find the next move the traceback alg should make
def next(Matrix, x, y):
    global total_score
    diag = Matrix[x-1][y-1]
    up = Matrix[x - 1][y]
    left = Matrix[x][y - 1]
    
    if diag >= up and diag >= left:     # Tie goes to the DIAG move.
        total_score = total_score + diag
        return 1 if diag != 0 else 0    # 1 signals a DIAG move. 
    elif up > diag and up >= left:      # Tie goes to UP move.
        total_score += up
        return 2 if up != 0 else 0      # UP move or end.
    elif left > diag and left > up:
        total_score += left
        return 3 if left != 0 else 0    # LEFT move or end.
    else:
        # Execution should not reach here.
        raise ValueError('invalid move during traceback')



f = open(sys.argv[1], 'r')
P1 = open("Param1data.txt", 'w')
pline = f.readline()

m = int(sys.argv[2])
s = float(sys.argv[3])
d = float(sys.argv[4])
if sys.argv[5] == 'a':
    a = True
else:
    a = False

total_score = 0
seq1 = seq2 = None
#go through the sequence file
while pline != "":
    if seq1 != None and seq2 != None:
        print("running...") 
        GO(seq1, seq2, a)
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

print("DONEDONEDONEDONEDONEDONEDONEDONE!!!!!!!!!")
