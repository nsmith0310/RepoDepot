###171

year = 1900
mon=7
count=0
while year<=2000:
    
    if year%4==0 and year!=1900:
        jan=31
        feb=29
        mar=31
        apr=30
        may=31
        jun=30
        jul=31
        aug=31
        sep=30
        ocb=31
        nov=30
        dec=31
        d=1
        while d!=-1:
            mon+=7
            if mon>jan:
                mon=mon-jan
                
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==jan:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>feb:
                mon=mon-feb
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==feb:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>mar:
                mon=mon-mar
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==mar:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>apr:
                mon=mon-apr
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==apr:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>may:
                mon=mon-may
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==may:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>jun:
                mon=mon-jun
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==jun:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>jul:
                mon=mon-jul
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==jul:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>aug:
                mon=mon-aug
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==aug:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>sep:
                mon=mon-sep
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==sep:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>ocb:
                mon=mon-ocb
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==ocb:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>nov:
                mon=mon-nov
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==nov:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>dec:
                mon=mon-dec
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==dec:
                mon=7
                d=-1
    else:
        jan=31
        feb=28
        mar=31
        apr=30
        may=31
        jun=30
        jul=31
        aug=31
        sep=30
        ocb=31
        nov=30
        dec=31
        d=1
        while d!=-1:
            mon+=7
            if mon>jan:
                mon=mon-jan
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==jan:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>feb:
                mon=mon-feb
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==feb:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>mar:
                mon=mon-mar
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==mar:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>apr:
                mon=mon-apr
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==apr:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>may:
                mon=mon-may
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==may:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>jun:
                mon=mon-jun
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==jun:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>jul:
                mon=mon-jul
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==jul:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>aug:
                mon=mon-aug
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==aug:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>sep:
                mon=mon-sep
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==sep:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>ocb:
                mon=mon-ocb
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==ocb:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>nov:
                mon=mon-nov
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==nov:
                mon=7
                d=-1
        d=1
        while d!=-1:
            mon+=7
            if mon>dec:
                mon=mon-dec
                if mon==1 and year > 1900:
                    count+=1
                d=-1
            elif mon==dec:
                mon=7
                d=-1
    year+=1
print(count)

                
                
            
