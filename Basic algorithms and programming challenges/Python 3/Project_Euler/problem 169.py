###178653872807
###translation of sage program on https://oeis.org/A002487

def bits(n):
    return bin(n)


def f(n):
    m = [1,0]
    e = list(map(int,list(bits(n)[2:])))

    ###not sure why this yields the correct answer, but the loop
    ###updates each of the m[a,b] values by summing the list and
    ###updating the value of the list equal to the bit value in the
    ###binary representation of n

    ###for example, if the number has 100 bits in binary, the loop
    ###runs 100 times
    for x in e:
        m[x]=m[0]+m[1]
    return m[1]


print(f(10**25 + 1))
