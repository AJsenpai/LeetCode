class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid = 0,0
        high = len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                self.swap(nums,low,mid)
                low +=1
                mid +=1
            elif nums[mid]==2:
                self.swap(nums,mid,high)
                high -=1
            else:
                mid +=1
                
    def swap(self,a,i,j):
        a[i],a[j]=a[j],a[i]
                