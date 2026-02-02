###answer 972 from 99^95
mx =0
final = []
i=0
j=0
n = 0
m =0
while i < 100:
  j=0
  while j < 100:
    test = list(str(pow(i,j)))
    test = list(map(int, test))
    pos = sum(test)
    
    if pos > mx:
      mx=pos
      n = i
      m = j
      final.append(mx)
    j+=1
  i+=1
print("Sum: " ,max(final), " from ", n, "^",m)

  
