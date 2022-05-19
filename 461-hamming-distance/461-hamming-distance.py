class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # do xor to get the count of no fo 1's in x and y
        # the calculate total no of 1's
        
        return bin(x^y).count('1')