###answr: 906609 from 913*993

num1=100
num2=100
i=899
palindromes=[]
while i <= 999:
    palindromes.append(int(str(i)+str(i)[::-1]))
    i+=1

mx=0
###palindromes.sort()
print(palindromes)
p=0
while num1 <= 999:
  num2=100
  while num2 <= 999:
    k=0
    while k < len(palindromes):
      if palindromes[k] == num1*num2:
        p = palindromes[k]
        if p >= mx:
          mx = p
          print("Largest: ", mx, "|num1: ", num1, "|num2: ", num2)

      k+=1
    num2+=1

  num1+=1
print("DONE!")

