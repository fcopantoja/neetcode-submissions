class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 0
        digits = digits[::-1]

        for i in range(len(digits)):
            if i == 0:
                val = digits[i] + 1 + carry
            else:
                val = digits[i] + carry

            carry = val // 10
            val = val % 10
            result.append(val)

        if carry:
            result.append(carry)
        
        return result[::-1]