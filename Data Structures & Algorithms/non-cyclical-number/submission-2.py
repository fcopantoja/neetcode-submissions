class Solution:
    def sum_of_squares(self, number: int):
        result = 0
        while number:
            digit = number % 10
            result += digit ** 2
            number = number // 10
        
        return result

    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n

        while True:
            number = self.sum_of_squares(number)
            if number == 1:
                return True
            if number in seen:
                return False
            
            seen.add(number)

        
        return False
