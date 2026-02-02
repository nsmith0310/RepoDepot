###15836928

###can be implemented in euler class

###2*a(n-1) + 2*a(n-2) - 2*a(n-3) + a(n-4), A181688 linear recursion

 

# Base Cases :

# F(1) = 1, F(2) = 1, F(3) = 4, F(4) =8

  

# A utility function to multiply two 

# matrices a[][] and b[][]. Multiplication 

# result is stored back in b[][]

def multiply(a, b):

      

    # Creating an auxiliary matrix 

    # to store elements of the

    # multiplication matrix

    ###

    mul = [[0 for x in range(4)]

              for y in range(4)];

    for i in range(4):

        for j in range(4):

            mul[i][j] = 0;

            for k in range(4):

                mul[i][j] += (a[i][k] * b[k][j]);

  

    # storing the multiplication

    # result in a[][]

    for i in range(4):

        for j in range(4):

            a[i][j] = mul[i][j]%10**8; # Updating our matrix

    return a;

  

# Function to compute F raise 

# to power n-2.

def power(F, n):

  

    M = [[2, 2,-2, 1], [1, 0, 0,0], [0, 1, 0,0],[0,0,1,0]];

  

    # Multiply it with initial values i.e 

    # with F(0) = 0, F(1) = 1, F(2) = 1

    if (n == 1):

        return F[0][0] + F[0][1];

  

    power(F, int(n / 2));

  

    F = multiply(F, F);

  

    if (n % 2 != 0):

        F = multiply(F, M);

  

    # Multiply it with initial values i.e 

    # with F(0) = 0, F(1) = 1, F(2) = 1

    return F[0][0] + F[0][1] ;

  

# Return n'th term of a series defined 

# using below recurrence relation.

# f(n) is defined as

# f(n) = f(n-1) + f(n-2) + f(n-3), n>=3

# Base Cases :

# f(0) = 0, f(1) = 1, f(2) = 1

def findNthTerm(n):

    F = [[2, 2, -2,1], [1, 0, 0,0], [0, 1, 0,0],[0,0,1,0]];

  

    return power(F, n - 2);

  

# Driver code

n = 10**12;

  

print(findNthTerm(n)%10**8);

  

# This code is contributed by mits
