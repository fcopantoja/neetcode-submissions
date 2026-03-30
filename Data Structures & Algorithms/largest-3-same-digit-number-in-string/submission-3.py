class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = float("-inf")
        n = len(num)
        for i in range(n - 3 + 1):
            print(i)
            r = i + 1
            seq = num[i]
            while r < n and (r - i + 1) <= 3:
                if num[i] == num[r]:
                    seq += num[r]
                    if len(seq) == 3:
                        largest = max(largest, int(seq))
                    print(largest)
                    r += 1
                else:
                    break

        if largest == 0:
            largest = "0" * 3
        else:
            if largest != float("-inf"):
                largest = str(largest)
            else:
                largest = ""


        return largest
