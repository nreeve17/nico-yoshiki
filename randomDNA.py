import string
import random
import sys

f = open(sys.argv[1], 'w')

seqs = []
def makeDNA(n):
    DNA = ['A','G','T','C']
    return DNA[n]

def makeSeqs(p, n):
    
    for j in range(0, p):
        i=0
        s = ''
        while i <= n:
            r = random.randint(0,3)
            s = s + makeDNA(r)
            i+=1
        print(">seq", j+1)
        firs = ">seq" + str(j+1) + '\n'
        print(s, '\n')
        sec = s + '\n\n'
        f.write(firs)
        f.write(sec)
        seqs.append(s)

def Stats(sex):
    a = t = g = c = 0 
    tot = 0
    
    #for i in range(len(sex)):
     #   print(sex[i], '\n')
        
        
    for i in range(0, len(sex)):
        x = sex[i]
        #print(sex[i])
        for j in range(len(x)):
            if x[j] == 'A':
                a+=1
                tot+=1
                continue
            elif x[j] == 'T':
                t+=1
                tot+=1
                continue
            elif x[j] == 'C':
                c+=1
                tot+=1
                continue
            elif x[j] == 'G':
                g+=1
                tot+=1
                continue

    pera = float(a/tot)
    pert = float(t/tot)
    perg = float(g/tot)
    perc = float(c/tot)

    print("% A in all seqs is ", pera)
    print("% T in all seqs is ", pert)
    print("% G in all seqs is ", perg)
    print("% C in all seqs is ", perc)



number = int(input("Number of sequences: "))
leng = int(input("Length of seqs: "))

makeSeqs(number, leng)
#print(seqs)
Stats(seqs)
