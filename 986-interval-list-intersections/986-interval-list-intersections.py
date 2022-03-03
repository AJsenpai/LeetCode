class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        
        intersect = []
        
        start,end = 0,1
        i,j = 0,0
        
        while i<len(a) and j<len(b):
            
            # a inside b
            a_overlaps_b = b[j][start]<= a[i][start] and a[i][start] <= b[j][end]
            
            # b inside a
            b_overlaps_a = a[i][start] <= b[j][start] and b[j][start] <= a[i][end]
        
            if a_overlaps_b or b_overlaps_a:
                intersect.append([max(a[i][start],b[j][start]), min(a[i][end],b[j][end])])
            
            # increment interval which is running behind
            if a[i][end] < b[j][end]:
                i += 1
            else:
                j += 1
    
        return intersect
    
        
        
        