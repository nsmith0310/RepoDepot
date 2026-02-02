class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff = []
        final = []
        for x in arr1:
            if x not in arr2:
                diff.append(x)
        diff.sort()
        l2 = []
        for x in arr2:
            l2.append([arr1.count(x),x])
        for x in l2:
            for j in range(0,x[0]):
                final.append(x[1])
        for x in diff:
            final.append(x)
        return final
