class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = [0 for i in range(0,num_people)]
        lim = len(people)-1
        i = 1
        while candies>=0:
            j = 0
            while j<=lim:
                if candies-i<0:
                    people[j]+=candies
                    return people
                else:
                    people[j]+=i
                    candies-=i
                
                i+=1
                j+=1
        return people
                
                
            
