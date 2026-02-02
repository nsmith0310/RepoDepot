class Solution:

    def f(self, s:str) -> int:

        if s=="I":

            return 1

        elif s=="IV":

            return 4

        elif s=="V":

            return 5

        elif s=="IX":

            return 9

        elif s=="X":

            return 10

        elif s=="XL":

            return 40

        elif s=="L":

            return 50

        elif s=="XC":

            return 90

        elif s=="C":

            return 100

        elif s=="CD":

            return 400

        elif s=="D":

            return 500

        elif s=="CM":

            return 900

        elif s=="M":

            return 1000

        else:

            return 0

    def romanToInt(self, s: str) -> int:

        s= s+" "

        t=0

        if len(s)==1:

            return f(s)

        else:

            i = 0

            while i<len(s)-1:

                if s[i]+s[i+1]=="IV" or s[i]+s[i+1]=="IX" or s[i]+s[i+1]=="XL" or s[i]+s[i+1]=="XC" or s[i]+s[i+1]=="CD" or s[i]+s[i+1]=="CM":

                    t+=self.f(s[i]+s[i+1])

                   

                    i+=2

                else:

                    t+=self.f(s[i])

                    i+=1

           

            return t
