class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance = x^2 + y^2
        
        maxheap = []        
        for i in range(len(points)):
            x,y = points[i]
            distance = (x*x)+(y*y)
            heappush(maxheap, (-distance, points[i]))
            
            if len(maxheap)>k:
                heappop(maxheap)
        
        closest_points = []
        while maxheap:
            distance,point = heappop(maxheap)
            closest_points.append(point)
        return closest_points
            
        