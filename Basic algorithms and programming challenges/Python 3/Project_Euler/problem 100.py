###Answer num = 756872327473 den = 1070379110497
i=1
xt = 15
yt = 21
while i!=-1:
    x = 3*xt + 2*yt - 2
    y = 4*xt + 3*yt - 3
    xt = x
    yt= y
    if yt > pow(10,12):
        print(xt,yt)
        break
    
