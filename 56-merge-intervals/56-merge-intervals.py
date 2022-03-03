class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        if len(intervals)<2:
            return intervals
        
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        
        for start,end in intervals[1:]:
            lastEnd = result[-1][-1]
            
            if start<=lastEnd:
                result[-1][-1] = max(end, lastEnd)
            else:
                result.append([start,end])
        return result
                
        
        

                