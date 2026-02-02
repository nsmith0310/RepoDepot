

class Solution:
    
    
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        A.sort(reverse=True)
        mx = 0
        i = 0
        while i<len(A)-2:
            num1 = A[i]
            j = i+1
            while j<len(A)-1:
                
                num2 = A[j]
                
                k = j+1
                while k<len(A):
                    num3 = A[k]
                    if num1+num2>num3 and num1+num3>num2 and num2+num3>num1:
                        return num1+num2+num3
                    else:
                        break
                    k+=1
                j+=1
            i+=1
        return mx
        
