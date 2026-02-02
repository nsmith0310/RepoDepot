###answer for numbers under 1 m: number is 837799 with 525 chains
print("Starting num:")
num=int(input())
i=2
k=i
mx=0
numb=0
count=0
while i < num:
    
    count=0
    k=i
    while k >1:
        if k%2==0:
            k=k/2
        else:
            k=3*k+1
        
        count+=1
        
    if mx < count:
        mx=count
        numb=i
    i+=1
print("Longest chain occurs with ", numb)
print("Number of links: ", mx+1)

###
    
