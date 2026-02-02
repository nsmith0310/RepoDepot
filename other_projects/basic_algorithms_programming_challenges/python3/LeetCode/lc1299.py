class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2 = []
        i = 1
        while i<len(arr):
            tmp = arr[i:]
            arr2.append(max(tmp))
            i+=1
        arr2.append(-1)
        return arr2
