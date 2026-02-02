###Answer: 127035954683 with a described solution from someone else (my code,
###their description)

def cube(n):
  x = n**3
  return x

def merge(n):
  l = list(map(int,list(str(cube(n)))))
  l.sort()
  l = list(map(str, l))
  l = ''.join(l)
  return l

def count(n,m):
    o = [item for sublist in n for item in sublist]
    for x in o:
        if o.count(x)==m:
            return o[o.index(x)+1]

n = 2
i = 1

print("Enter number of permutations: ")
p = int(input())

while n!=-1:
    tmp=[]
    while len(merge(i))<n:
        tmp.append([merge(i),i])
        i+=1
    if count(tmp, p)!=None:
        print(count(tmp, p),": ", (count(tmp, 5))**3 )
        break
    n+=1

