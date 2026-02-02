###answer: 161667

###I in no way designed the top two methods

import numpy as np

 

def gen_prim_pyth_trips(limit=None):

    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')

    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')

    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')

    uad = np.array([u, a, d])

    m = np.array([3, 4, 5])

    while m.size:

        m = m.reshape(-1, 3)

        if limit:

           m = m[m[:, 2] <= limit]

        yield from m

        m = np.dot(m, uad)

 

def trips(limit):

    tmp=[]

    for prim in gen_prim_pyth_trips(limit):

        i = prim

        for _ in range(limit//prim[2]):

            tmp.append(i)

            i = i + prim

    x = np.array(tmp).tolist()

    return x

           

f = trips(1500000)

y=[]

for x in f:

    if sum(x)<=1500000:

        y.append(sum(x))

 

u, c = np.unique(y, return_counts=True)

 

x = np.array(c).tolist()

z = list(filter(lambda v: v<2, x))

print(len(z))
