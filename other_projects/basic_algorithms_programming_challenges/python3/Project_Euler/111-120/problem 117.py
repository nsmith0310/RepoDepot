###100808458960497

###major help from dreamshire for suggesting tetranacci numbers

 

t =[0,0,0,1]

 

while len(t)<=53:

    t.append(t[-1]+t[-2]+t[-3]+t[-4])

   

print(t[-1])
