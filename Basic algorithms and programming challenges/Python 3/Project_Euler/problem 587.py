###2240
###major hints by https://mathproblems123.wordpress.com/2017/01/27/about-problem-587-project-euler/

import numpy as np
from math import pi as pie,sqrt

pi = pie

def quad(a,b,c):
    return [(-b + sqrt(b**2 - 4*a*c))/(2*a),(-b - sqrt(b**2 - 4*a*c))/(2*a)]


def xy(n):
    c = (1/n)**2
    a = 1+c
    
    b = -1 - (1/n)
    c = .25
    x = quad(a,b,c)[1]
    
    z = (.5-x)**2
    y = x/n
    return [x,y]
def angle(s):
    l = .5 - s**2
    l2 = .5
    n = l/l2
    return np.arccos(n)


def a(x,y):
    A = angle(1-2*y)
    
    B = (.25/2)*((A-np.sin(A)))
    
    C = pi/8 - B
    
    D = .5 - x - C
    return D/2
    

    
def tri(n):
    k = xy(n)
    x = k[0]
    y = k[1]
    area = (x*y)/2
    
    area2 = a(x,y)
    
    return (area+area2)/2



A = (1/8)-(pi/32)

n = 1
while (tri(n)/A)>=.001:
    n+=1
print(n)

