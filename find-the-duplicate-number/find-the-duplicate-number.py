class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if nums[i]!= i+1:
                j = nums[i]-1
                if nums[i]!= nums[j]:
                    self.swap(nums,i,j)
                else:
                    return nums[i]
            else:
                i +=1
    def swap(self,a,i,j):
        a[i],a[j]=a[j],a[i]
            
