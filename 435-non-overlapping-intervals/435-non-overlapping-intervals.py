class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        start,end = 0,1
        
        not_overlap = 0
        lastEnd = intervals[0][-1]
        
        for interval in intervals[1:]:
            if interval[start] < lastEnd:             # curr_start<lastEnd, overlapping   
                
                # to find max overlapping we need min end , greedy
                lastEnd = min(lastEnd, interval[end]) 

                
            else:
                not_overlap += 1
                lastEnd = interval[end]
        
        return (len(intervals)-1) - (not_overlap)