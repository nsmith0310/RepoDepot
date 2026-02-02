###ANSWER: (SLOW): d = 983 with cycle length = 982
print("Limit:")
lim = int(input())
i = 2
j = 0
count = 0
mx = 0
num = 0
while i < lim:
  current = 1
  tmp = []
  j=0
  count=0
  while j!=-1:
    current = 10*current%i
    tmp.append(current)
    count+=1
    if count-1 > mx:
      mx = count-1
      num = i
    for x in tmp:
      if tmp.count(x)==2 or current==0:
        j=-2
    ###print(current)
    j+=1
  
  if count-1 > mx:
    mx = count-1
    num = i

  i+=1

print("Max cycle: ", mx, "for d =", num)
