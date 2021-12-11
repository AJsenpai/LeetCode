class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # put all the weight on rightside first
        # check if left and right side are matching 
        # if not- move the curr weight to left side
        left_side_wt,right_side_wt = 0,sum(nums)
        for idx,curr_weight in enumerate(nums):
            right_side_wt -= curr_weight
            if left_side_wt == right_side_wt:
                return idx
            left_side_wt += curr_weight
        return -1

            
            
        