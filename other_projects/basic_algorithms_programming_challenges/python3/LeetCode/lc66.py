class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = list(map(str,digits))
        num2 = int(''.join(num))+1
        num3=list(str(num2))
        return num3
