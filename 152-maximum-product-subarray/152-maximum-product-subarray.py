class Solution:
    def maxProduct(self, a: List[int]) -> int:
        max_product = float('-inf')
        positive_prod = 1
        negative_prod = 1
        
        for num in a:
            x = max(num, positive_prod*num, negative_prod*num)
            y = min(num, positive_prod*num, negative_prod*num)
            positive_prod, negative_prod = x, y
            max_product = max(max_product, positive_prod)
        return max_product
            