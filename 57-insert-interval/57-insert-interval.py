class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i,start,end = 0,0,1
        
        # append all the intervals less which comes before new interval
        while i<len(intervals) and intervals[i][end]< newInterval[start]:
            merged.append(intervals[i])
            i += 1
        
        # merge conflicting intervals
        while i<len(intervals) and intervals[i][start]<= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1
        
        merged.append(newInterval)
        
        while i<len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
        