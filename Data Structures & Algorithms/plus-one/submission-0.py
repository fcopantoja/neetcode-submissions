class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                val = digits[i] + 1 + carry
            else:
                val = digits[i] + carry

            carry = val // 10
            val = val % 10
            result.append(val)

        if carry:
            result.append(carry)
        
        return result[::-1]