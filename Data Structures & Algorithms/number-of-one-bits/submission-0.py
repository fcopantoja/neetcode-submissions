class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_result = ["0"] * 32
        count = 0

        for i in range(32):
            print(n)
            if n % 2 == 1:
                binary_result[31 - i] = "1"
                count += 1
            
            n = n // 2
        
        return count
