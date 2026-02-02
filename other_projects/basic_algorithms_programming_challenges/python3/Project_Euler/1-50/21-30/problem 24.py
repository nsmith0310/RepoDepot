import itertools
all = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
all.sort()
print(all[999999])
i=0
num=""
while i < len(all[999999]):
    num = num + str(all[999999][i])
    i+=1
print(num)
