class Solution:
    def get_sum(self, number: int):
        digits = [int(x) for x in str(number)]
        a = 0
        for digit in digits:
            a += digit ** 2
        return a

    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n

        while True:
            number = self.get_sum(number)
            if number == 1:
                return True
            if number in seen:
                return False
            
            seen.add(number)

        
        return False
