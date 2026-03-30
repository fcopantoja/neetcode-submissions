class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        for c in arr:
            counts[c] += 1

        kth_idx = 1

        for key, value in counts.items():
            if value == 1:
                if kth_idx == k:
                    return key
                kth_idx += 1

        return ""


