class Solution:
    def sortColors(self, a: List[int]) -> None:
        
        low,mid,high = 0,0,len(a)-1
        
        while mid<=high:
            if a[mid]==0:
                self.swap(a,mid,low)
                low += 1
                mid += 1
                            
            elif a[mid]==2:
                self.swap(a,mid,high)
                # since we are going left to right number at right 
                # is not processed after swap so we cant increment mid
                high -=1
            
            elif a[mid]==1:
                mid += 1

        return a
            
    
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]
        