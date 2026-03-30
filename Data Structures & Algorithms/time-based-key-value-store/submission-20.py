class TimeMap:
    def __init__(self):
        self.hash_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_dict:
            self.hash_dict[key][timestamp] = value
        else:
            self.hash_dict[key] = {timestamp: value}
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.hash_dict)
        print(key, timestamp)
        value = self.hash_dict.get(key, {}).get(timestamp)
        if not value:
            i = timestamp - 1
            while i > 0:
                value = self.hash_dict.get(key, {}).get(i)
                if value: break
                i -= 1
            if not value:
                value = ""
        return value
    
