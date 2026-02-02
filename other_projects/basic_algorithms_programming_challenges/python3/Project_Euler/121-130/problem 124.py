###ANSWER: 21417

from euler import factorize
from numpy import prod

tmp = []
i = 1
while i <=100000:
    tmp.append([prod(list(dict.fromkeys(factorize(i)))),i])
    i+=1
new = sorted(tmp, key = lambda x: x[0])

print(new[9999][1])

