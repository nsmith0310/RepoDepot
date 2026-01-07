print("First index of number with n digits, n=")
digs = int(input())
i = 1
j = 1

lst = []
count = 0
while count > -1:
    lst.append(i)
    lst.append(j)
    j=j+i
    i=i+j
    lst.sort()
    if len(str(lst[count])) == digs:
        print(count + 1)
        print(lst[count])
        break
    count+=1
    

