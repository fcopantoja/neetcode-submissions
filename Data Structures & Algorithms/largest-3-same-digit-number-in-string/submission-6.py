class Solution:
    def largestGoodIntegerNaive(self, num: str) -> str:
        largest = float("-inf")
        n = len(num)
        for i in range(n - 3 + 1):
            r = i + 1
            while r < n and (r - i + 1) <= 3:
                if num[i] == num[r]:
                    if r - i + 1 == 3:
                        largest = max(largest, int(num[r]))
                    r += 1
                else:
                    break

        return str(largest) * 3 if largest != float("-inf") else "" 

    
    def largestGoodInteger(self, num: str) -> str:
        res = "0"

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, num[i: i + 3])
                print(res)

        return res if res != "0" else ""

