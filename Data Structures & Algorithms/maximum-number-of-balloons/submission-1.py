class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter1 = Counter(text)

        return min(
            counter1["b"],
            counter1["a"],
            counter1["l"] // 2,
            counter1["o"] // 2,
            counter1["n"],
        )