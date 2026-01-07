###Answer: 1118049290473932
###my solution, based on the wiki approach
###l[2] = 19*l[1]-l[1]-l[2]

l = [17,305]

count = 1
while count< 11:
    l.append((l[count]*19)-l[count]-l[count-1])
    count+=1
print(len(l))
print(sum(l))
