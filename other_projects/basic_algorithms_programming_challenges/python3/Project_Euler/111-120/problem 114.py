###16475640049

###A005252

 

t = [1,1,1,1, 2, 4, 7]

 

while len(t)<=51:

    t.append(2*t[-1]-t[-2]+t[-4])

   

t.remove(t[0])

t.remove(t[1])

print((t[-1]))
