import os
import string

P1 = open("Param1data.txt", 'r')
P2 = open("Param2data.txt", 'r')

place = open('p1counts.csv', 'w')
place2 = open('p2counts.csv', 'w')

line = str(P1.readline()).strip('\n')

counts = {}

while line != "":
    if line in counts:
        
        counts[line]+=1
        line = P1.readline().strip('\n')
    else:
        counts.update({line:1})
        #counts[line]+=1
        line = P1.readline().strip('\n')

for key, value in counts.items():
    print(key, value)
    place.write(key)
    place.write(",")
    place.write(str(value))
    place.write('\n')

print('\n')
line = str(P2.readline()).strip('\n')

counts2 = {}

while line != "":
    if line in counts2:
        
        counts2[line]+=1
        line = P2.readline().strip('\n')
    else:
        counts2.update({line:1})
        #counts[line]+=1
        line = P2.readline().strip('\n')

for key, value in counts2.items():
    print(key, value)
    place2.write(key)
    place2.write(",")
    place2.write(str(value))
    place2.write('\n')

totalsum = 0
avgnum = 10
for key, value in counts.items():
    totalsum += (int(key)*value)
    #avgnum+=1

avg = float(totalsum/avgnum)
print("avg len of p1 is : ", avg)
"""
totalsum = 0
for key, value in counts2.items():
    totalsum += (int(key)*value)

avg = float(totalsum/500)
print("avg len of p2 is : ", avg)
"""
