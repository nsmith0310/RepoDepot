###Answer: 333082500 (R: I already found the answer using a slow
###algorithm of my own making: this one is much faster, though I used
###two statements which I don't understand (the code is of my own making))

def rem(x):
  if x%2==0:
    ###bellow are the two statements
    top = (x-2)*x
  else:
    top = (x-1)*x
  return top

count = 0
i = 3
while i <= 1000:
  count+=rem(i)
  i+=1
print(count) 
