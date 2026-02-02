###answer: 669171001

print("Enter n of nxn dimensions (1001x1001 is problem): ")
num = int(input())
count = 1
odd = 3
nums=[]
while odd <=num:
    while count < odd*odd:
        count = count + (odd-1)
        nums.append(count)
    odd+=2
nums.append(1)
print("Sum of diagonals: ", sum(nums))
