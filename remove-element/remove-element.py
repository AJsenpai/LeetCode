class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        boundary = 0
        for i in range(len(nums)):
            if nums[i] != val:
                self.swap(nums, i, boundary)
                boundary += 1
        return boundary

    def swap(self, a, i, j):
        a[i], a[j] = a[j], a[i]