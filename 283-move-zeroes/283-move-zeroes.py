class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # capture non zero from front
        non_zero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                self.swap(nums,non_zero,i)
                non_zero += 1
        return nums

    
    def swap(self,a,i,j):
        a[i],a[j] = a[j],a[i]