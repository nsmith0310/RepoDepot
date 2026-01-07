###7273
###basically Dijkstra's algorithm

l = [line.rstrip('\n') for line in open("triangle.txt")]

nums=[]
for x in l:
    nums.append(list(map(int,x.split(" "))))
nums.append([0 for i in range(0,101)])

t=0
for x in nums[1:-1]:
    for y in x:
        if x.index(y)!=0 and x.index(y)!=len(x)-1:
            ###print(x)
            n1 = nums[nums.index(x)-1][x.index(y)]
            n2 = nums[nums.index(x)-1][x.index(y)-1]
            if y+n1>y+n2:
                x[x.index(y)]+=n1
            else:
                x[x.index(y)]+=n2
        elif x.index(y)==0:
            n1 = nums[nums.index(x)-1][x.index(y)]
            x[x.index(y)]+=n1
        else:
            n1 = nums[nums.index(x)-1][x.index(y)-1]
            x[x.index(y)]+=n1
            
print(max(nums[-2]))
