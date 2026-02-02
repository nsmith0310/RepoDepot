###Answer 228
###used gg solution of adding up triangles using (0,0) as vertex
###of component trinagles: if the three components add up to the
###given triangle, the point cant lie outside of the triangle

filepath = 'triangles.txt'

tri = []

with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       tri.append((line.strip()))
       line = fp.readline()
       cnt += 1


def check(s):
    v0=0
    v1=0
    x1 = int(s.split(",")[0])
    y1 = int(s.split(",")[1])
    x2 = int(s.split(",")[2])
    y2 = int(s.split(",")[3])
    x3 = int(s.split(",")[4])
    y3 = int(s.split(",")[5])

    a = abs(((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2)))/2)
    
    a1 = abs(((x1*(v1-y3))+(v0*(y3-y1))+(x3*(y1-v1)))/2)
    
    a2 = abs(((x1*(y2-v1))+(x2*(v1-y1))+(v0*(y1-y2)))/2)
    
    a3 = abs(((v0*(y2-y3))+(x2*(y3-v1))+(x3*(v1-y2)))/2)
    
    
    if a1+a2+a3==a:
        return True
    else:
        return False
    
count=0
for x in tri:
    if(check(x))==True:
        count+=1
print(count)
    

