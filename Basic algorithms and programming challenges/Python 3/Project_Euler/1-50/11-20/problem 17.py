###fix second digt in hundreds for 0 cases
###ANSWER: 21124

def ct(n):
    num = 0
    count=0
    l = len(str(n))
    n = str(n)
    if l == 3:
        if n[0]=='1':
            count=3 +7 + 3
            count+=gg((str(n)[1:]))
        if n[0]=='2':
            count=3 +7+ 3
            count+=gg((str(n)[1:]))
        if n[0]=='3':
            count=5 +7+ 3
            count+=gg((str(n)[1:]))
        if n[0]=='4':
            count=4 +7+ 3
            count+=gg((str(n)[1:]))
        if n[0]=='5':
            count=4 +7+ 3
            count+=gg((str(n)[1:]))
        if n[0]=='6':
            count=3 +7+ 3
            count+=gg((str(n)[1:]))
        if n[0]=='7':
            count=5 +7+ 3
            count+=gg((str(n)[1:]))
        if n[0]=='8':
            count=5 +7+ 3
            count+=gg((str(n)[1:]))
        if n[0]=='9':
            count=4 +7+ 3
            count+=gg((str(n)[1:]))
    if l ==2:
        if n[0]=='1':
            if n[1]=='1':
                count = 6
            if n[1]=='2':
                count = 6
            if n[1]=='3':
                count = 8
            if n[1]=='4':
                count = 8
            if n[1]=='5':
                count = 7
            if n[1]=='6':
                count = 7
            if n[1]=='7':
                count = 9
            if n[1]=='8':
                count = 8
            if n[1]=='9':
                count = 8
        if n[0]=='2':
            count=6
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
        
        if n[0]=='3':
            count=6
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
        if n[0]=='4':
            count=5
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
        if n[0]=='5':
            count=5
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
        if n[0]=='6':
            count=5
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
        if n[0]=='7':
            count=7
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
        if n[0]=='8':
            count=6
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
        if n[0]=='9':
            count=6
            if n[1]=='1':
                count+=3
            if n[1]=='2':
                count+=3
            if n[1]=='3':
                count+=5
            if n[1]=='4':
                count+=4
            if n[1]=='5':
                count+=4
            if n[1]=='6':
                count+=3
            if n[1]=='7':
                count+=5
            if n[1]=='8':
                count+=5
            if n[1]=='9':
                count+=4
    if l ==1:
        if n=='1':
            count=3
        if n=='2':
            count=3
        if n=='3':
            count=5
        if n=='4':
            count=4
        if n=='5':
            count=4
        if n=='6':
            count=3
        if n=='7':
            count=5
        if n=='8':
            count=5
        if n=='9':
            count=4
    return count
        
def gg(n):
    count=0
    if n[0]=='0':
        if n[1]=='1':
            count = 3
        if n[1]=='2':
            count = 3
        if n[1]=='3':
            count = 5
        if n[1]=='4':
            count = 4
        if n[1]=='5':
            count = 4
        if n[1]=='6':
            count = 3
        if n[1]=='7':
            count = 5
        if n[1]=='8':
            count = 5
        if n[1]=='9':
            count = 4
    if n[0]=='1':
        if n[1]=='0':
            count+=3
            
        if n[1]=='1':
            count = 6
        if n[1]=='2':
            count = 6
        if n[1]=='3':
            count = 8
        if n[1]=='4':
            count = 8
        if n[1]=='5':
            count = 7
        if n[1]=='6':
            count = 7
        if n[1]=='7':
            count = 9
        if n[1]=='8':
            count = 8
        if n[1]=='9':
            count = 8
    if n[0]=='2':
        count=6
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
            count+=4
        
    if n[0]=='3':
        count=6
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
            count+=4
    if n[0]=='4':
        count=5
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
            count+=4
    if n[0]=='5':
        count=5
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
                count+=4
    if n[0]=='6':
        count=5
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
            count+=4
    if n[0]=='7':
        count=7
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
            count+=4
    if n[0]=='8':
        count=6
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
            count+=4
    if n[0]=='9':
        count=6
        if n[1]=='0':
            count+=0
        if n[1]=='1':
            count+=3
        if n[1]=='2':
            count+=3
        if n[1]=='3':
            count+=5
        if n[1]=='4':
            count+=4
        if n[1]=='5':
            count+=4
        if n[1]=='6':
            count+=3
        if n[1]=='7':
            count+=5
        if n[1]=='8':
            count+=5
        if n[1]=='9':
            count+=4
    return count

nums = [i for i in range(1,1000)]
nums.remove(100)
nums.remove(200)
nums.remove(300)
nums.remove(400)
nums.remove(500)
nums.remove(600)
nums.remove(700)
nums.remove(800)
nums.remove(900)

total = 113

for x in nums:
    total+=ct(x)

print(total)
