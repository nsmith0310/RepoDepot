###Answer: 40730
from math import factorial
print("Enter upper limit: ")
lim = int(input())
i=0
j=0
curious=[]
tmp_str=[]
###tmp_int=[]
tmp_fact=[]
while i < lim:
    j=0
    tmp_fact=[]
    tmp_str=[]
    tmp_int=[]
    tmp_str = list(str(i))
    tmp_int=list(map(int, tmp_str))
    while j < len(tmp_int):
        tmp_fact.append(factorial(tmp_int[j]))
        j+=1
    if sum(tmp_fact)==i and sum(tmp_fact)!=1 and sum(tmp_fact)!=2:
        curious.append(i)
    i+=1
print("Curious numbers:")
print(curious)
print("Their sum:")
print(sum(curious))
