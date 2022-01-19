class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        if len(a)==1:
            return 0
        
        start,end = 0,len(a)-1
        while start<=end:
            # left | mid | right
            mid = start + (end - start) // 2
            left = a[mid - 1] if mid > 0 else float('-inf')
            right = a[mid + 1] if mid < len(a) - 1 else float('-inf')

            # print(mid,left,right)
            if left < a[mid] and right > a[mid]:  # right greater
                start = mid + 1
            elif left > a[mid] and right < a[mid]:  # left greater
                end = mid - 1
            elif left > a[mid] and right > a[mid]:  # both greater - go either way
                end = mid - 1
            else:
                return mid
        return -1
#             mid = start + (end-start)//2          
#             if mid > 0 and mid<len(a)-1:
#                 if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
#                     return mid
#                 elif a[mid-1] > a[mid]:
#                     end = mid - 1
#                 elif a[mid+1] > a[mid]:
#                     start = mid +1
#             else:
#                 # edge case
#                 if mid==0:
#                     if a[0] > a[1]:
#                         return 0
#                     else:
#                         return 1
                
                
#                 elif mid==len(a)-1:
#                     n = len(a)
#                     if a[n-1] > a[n-2]:
#                         return n-1
#                     else:
#                         return n-2
                        
                    
            
        