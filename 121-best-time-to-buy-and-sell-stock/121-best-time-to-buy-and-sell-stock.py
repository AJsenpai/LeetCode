class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_so_far = float(inf)
        for p in prices:
            min_so_far = min(min_so_far, p)
            current_profit = p - min_so_far
            max_profit = max(max_profit,current_profit)
        return max_profit
        