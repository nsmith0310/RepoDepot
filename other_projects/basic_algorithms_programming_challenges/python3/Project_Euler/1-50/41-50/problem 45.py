###SLOW: 1533776805

i=1
j=1
k=1
print("Enter test limit:")
lim=int(input())
print("Enter nth equality:")
end=int(input())

x = 0
y = 0
z = 0
count=0
while count!=end:
  count=0
  x = i*(i+1)/2
  j=0
  while j < i:
    k=0
    y = j*((3*j)-1)/2
    if x == y: 
      while k < j:
        z = k*((2*k)-1)
        if z == y == x:
          print(x, "for tri n=",i, " for pent l=", j)
          print("for hex o=", k)
          count+=1
          break
        k+=1
    j+=1
  i+=1

  

                
