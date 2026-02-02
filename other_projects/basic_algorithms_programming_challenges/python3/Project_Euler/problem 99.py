###SLOW: 709
from math import sqrt

bases = []
exps = []
reduced_b=[]
reduced_e=[]

test=[]
tmp=[]

f = open('base_exp.txt')
line = f.readline()
while line:
    x =line.partition(",")[0]
    bases.append(x)
    line = f.readline()
f.close()

f = open('base_exp.txt')
line = f.readline()
while line:
    x =line.partition(",")[2]
    y = x.partition("\n")[0]
    exps.append(y)
    line = f.readline()
f.close()

i = 0
while i < len(bases):
    reduced_b.append(int(bases[i]))
    reduced_e.append(int(exps[i]))
    i+=1

tmp_b = 0
tmp_e = 0
i = 0
mx = 0
largest = 0
while i < len(reduced_b):
    if reduced_b[i]**reduced_e[i] > mx:
        mx = reduced_b[i]**reduced_e[i]
        largest = i + 1
    print(i)
    i+=1
print(largest)

    
