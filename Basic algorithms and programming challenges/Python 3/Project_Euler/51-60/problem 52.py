'''1: 142857 (ANSWER)
2: 285174
3: 428571
4: 571428
5: 714285
6: 857142

'''

print("Enter number of multiples:")
mult=int(input())
i=1
j=1
tmp=[]
tmp_num=[]
count=0
tmp_i=[]
while i != -1:
    tmp=[]
    tmp_i=[]
    k=0
    j=1
    count=0
    while j <= mult:
        tmp_num=[]
        tmp_num=list(str(i*j))
        tmp_num.sort()
        ###print(tmp_num)
        tmp.append(''.join(tmp_num))
        ###print(tmp)
        j+=1
        
    tmp_i=list(str(i))
    tmp_i.sort()
    while k < len(tmp):
        if ''.join(tmp_i) == tmp[k]:
            count+=1
        k+=1
    if count == len(tmp):
        print(i)
        break
    i+=1
        
