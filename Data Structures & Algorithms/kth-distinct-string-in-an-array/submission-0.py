class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        for c in arr:
            counts[c] += 1

        idx = 1
        for key, value in counts.items():
            if value == 1:
                if idx == k:
                    return key
                idx += 1

        return ""


