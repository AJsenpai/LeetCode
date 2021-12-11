class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = right = -1
        max_so_far = float("-inf")
        for i in range(len(nums)):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < max_so_far:
                right = i

        min_so_far = float("inf")
        for i in reversed(range(len(nums))):
            min_so_far = min(min_so_far, nums[i])
            if nums[i] > min_so_far:
                left = i

        if left == -1:
            return 0
        return right - left + 1