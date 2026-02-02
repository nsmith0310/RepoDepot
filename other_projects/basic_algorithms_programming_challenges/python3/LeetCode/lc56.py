class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        i = 0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][1]:
                del intervals[i+1]
                i-=1
            elif intervals[i][1]<intervals[i+1][1] and intervals[i][1]>=intervals[i+1][0]:
                tmp = [intervals[i][0],intervals[i+1][1]]
                intervals[i] = tmp
                del intervals[i+1]
                i-=1
            i+=1
        
        return intervals
