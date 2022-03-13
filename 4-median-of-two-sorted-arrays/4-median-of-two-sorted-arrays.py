class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        total = len(A)+len(B)
        half = total//2
        
        # always keeping a smaller:
        if len(B)<len(A):
            A,B = B,A
        
        start,end = 0,len(A)-1
        
        while True:
            i = (start+end)//2 # a
            j = half - i - 2 # b
            
            A_left = A[i] if i>=0 else float('-inf')
            A_right = A[i+1] if (i+1) < len(A) else float('inf')
            B_left = B[j] if j>=0 else float('-inf')
            B_right = B[j+1] if (j+1) < len(B) else float('inf')
            
            # partition is correct
            if A_left <= B_right and B_left <= A_right:
                if total%2: # odd
                    return min(A_right, B_right)
                return (max(A_left,B_left) + min(A_right,B_right))/2
            
            elif A_left > B_right: # incorrect partition
                end = i-1
            else:
                start = i+1
            
            
        
        