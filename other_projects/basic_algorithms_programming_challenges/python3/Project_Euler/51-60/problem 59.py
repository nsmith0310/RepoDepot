###129448

from itertools import product as p
l = [line.rstrip('\n') for line in open("cipher.txt")]
words = [line.rstrip('\n') for line in open("wordlist.txt")]
li = []
nums=[]
for x in l:
    nums.append(list(map(int,x.split(","))))
for x in words:
    li.append(x.split(" ")[0])


l2 = [x for x in nums[0]]
c2=[]
m = list(p([k for k in range(97,123)],repeat=3))
v=[35,36,37,38,40,41,60,61,62,93,94,95,123,124,125,126,127,45,47,64]
end = 0
for x in m:
    if end==1:
        break
    d = [k for k in l2]
    kill=0
    i = 0
    while i<len(d):
        d[i]=d[i]^x[0]
        i+=3
    i = 1
    while i<len(d):
        d[i]=d[i]^x[1]
        i+=3
    i = 2
    while i<len(d):
        d[i]=d[i]^x[2]
        i+=3
    i = 1
    while i<len(d):
        if d[i]<=31:
            kill=1
            break
        if d[i] in v and d[i-1] in v:
            kill=1
            break
        i+=1
    
    if kill==0:
        tmp = [chr(j) for j in d]
        
        tmp2=((''.join(tmp))).split(" ")
        for z in tmp2:
            if len(z)>5 and z in li:
                print(tmp2)
                
                end = 1
                break
            elif len(z)>5 and z not in li:
                break
