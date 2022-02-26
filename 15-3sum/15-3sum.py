class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        if not a :
            return []
        
        # O(nlogn + n*n)  --> O(n^2) T
        
        a.sort()        
        result = []        
        for i in range(len(a)-2):
            
            # check for duplicates
            if i>0 and a[i]==a[i-1]:
                continue
                
            left,right = i+1, len(a)-1
            
            while left<right:
                curr_sum = a[i] + a[left] + a[right]
                
                if curr_sum==0:
                    result.append([a[i],a[left],a[right]])
                    
                    # another check for duplicate
                    while left<right and a[left]==a[left+1]:
                        left +=1
                    while left<right and a[right]==a[right-1]:
                        right -= 1
                    
                    
                    left += 1
                    right -= 1
                
                elif curr_sum > 0:
                    right -=1
                
                elif curr_sum < 0:
                    left +=1
        
        return result
                
        