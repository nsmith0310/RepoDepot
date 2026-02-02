###SLOW: 329468

def u(s):
  return len(set(s)) == len(s)
def fprep(s):
  v = s[:9]
  if "0" not in v:
    return u(v)
def bprep(s):
  v = s[::-1][:9]
  if "0" not in v:
    return u(v)
i = 1
j = 1
count = 0
while count!=-1:
  i+=j
  j+=i
  si = str(i)
  sj = str(j)
  if len(si)>=18:
    if fprep(si) == True and bprep(si)==True:
      print(count-1+4)
      break
  if len(sj)>=18:
    if fprep(sj) == True and bprep(sj)==True:
      print(count+4)
      break
  count+=2
