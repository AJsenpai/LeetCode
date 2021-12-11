class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in reversed(range(n)):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            # digits[i] = 0  # if last digit is 9

        new_num = [0] * (n + 1)
        new_num[0] = 1
        return new_num