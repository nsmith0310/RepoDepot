###SLOW: 8581146

def r_sq(num):
  tmp = list(str(num))
  tmp = list(map(int, tmp))
  tmp2=[]
  for x in tmp:
    tmp2.append(x**2)
  sq = sum(tmp2)
  return sq
count = 0
i = 1

print("Limit: ")
num = int(input())
while i < num:
  j = r_sq(i)
  while j != 1 and j!=89:
      j = r_sq(j)
  if r_sq(j)!=1:
      count+=1
  i+=1

print("Number of chains ending in 89 bellow ", num, ": ", count)
