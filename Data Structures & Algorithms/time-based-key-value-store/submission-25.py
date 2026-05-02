class TimeMap:
    def __init__(self):
        self.hash_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hash_dict[key]
        l = 0
        r = len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res