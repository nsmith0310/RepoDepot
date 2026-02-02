print("Enter max val: ")
max_val=int(input())

i = 1
sum_squares=0
square_sums=0

while i<max_val+1:
    sum_squares=sum_squares+(i*i)
    i+=1

i=1
while i < max_val+1:
    square_sums=square_sums+i
    i+=1
print("Square of sums from 1 to ", max_val, "minus square of sums from 1 to ", max_val, ": ")
print((square_sums*square_sums)-sum_squares)
