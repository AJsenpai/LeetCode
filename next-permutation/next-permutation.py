class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end =len(nums)-1
        while end-1>=0 and nums[end-1]>=nums[end]:
            end-=1
        if end==0:
            self.reverse(nums,0,len(nums)-1)
            return
        
        # pivot: array has a peak which is not at 0
        pivot = end-1 # actual pivot is i-1        
        successor = self.findSuccessor(nums,pivot,len(nums)-1)
        self.swap(nums,pivot,successor)        
        self.reverse(nums,pivot+1,len(nums)-1)
    
    def findSuccessor(self,a,pivot,end):
        for i in range(end,pivot,-1):
            if a[i]>a[pivot]:
                return i

                
    def reverse(self,a,start,end):
        while start<end:
            self.swap(a,start,end)
            start+=1
            end-=1            
    
    def swap(self,a,i,j):
        a[i],a[j]=a[j],a[i]
        
                
            
        
        
            