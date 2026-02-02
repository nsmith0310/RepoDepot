import string as s

def getNum(letter):
    num = letter
    if letter == 'A':
        num = 1
    if letter == 'B':
        num = 2
    if letter == 'C':
        num = 3
    if letter == 'D':
        num = 4
    if letter == 'E':
        num = 5
    if letter == 'F':
        num = 6
    if letter == 'G':
        num = 7
    if letter == 'H':
        num = 8
    if letter == 'I':
        num = 9
    if letter == 'J':
        num = 10
    if letter == 'K':
        num = 11
    if letter == 'L':
        num = 12
    if letter == 'M':
        num = 13
    if letter == 'N':
        num = 14
    if letter == 'O':
        num = 15
    if letter == 'P':
        num = 16
    if letter == 'Q':
        num = 17
    if letter == 'R':
        num = 18
    if letter == 'S':
        num = 19
    if letter == 'T':
        num = 20
    if letter == 'U':
        num = 21
    if letter == 'V':
        num = 22
    if letter == 'W':
        num = 23
    if letter == 'X':
        num = 24
    if letter == 'Y':
        num = 25
    if letter == 'Z':
        num = 26
    return num

text_file = open('names.txt')
text_lines1 = []
for x in text_file:
    text_lines1.append(x)
text_file.close()
text_lines1.sort()

text_lines = "".join(text_lines1)

text_lines3 = text_lines.replace('"', '')

text_lines4 = text_lines3.replace(',', ' ')

best_lines = text_lines4.split()
best_lines.sort()


tmp=[]
i = 1
j=0
tally = 0
count=0
print(list(best_lines[1]))


while i < len(best_lines):
    j=0
    count=0
    tmp=[]
    tmp = list(best_lines[i-1])
    while j < len(tmp):
        count=count+getNum(tmp[j])
        j+=1
    tally = tally + count*(i)
    
    i+=1

print("Sum of alpha-num translated names times position in list: ", tally)


        

   
