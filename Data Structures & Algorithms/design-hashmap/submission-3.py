class MyHashMap:

    def __init__(self):
        self.capacity = 32
        self.hash_arr = [[] for _ in range(self.capacity)]
        self.size = 0

    def _hash(self, key):
        return key % self.capacity

    def _rehash(self):
        old_arr = self.hash_arr
        self.capacity *= 2
        self.size = 0
        self.hash_arr = [[] for _ in range(self.capacity)]

        for bucket in old_arr:
            for tup in bucket:
                self.put(tup[0], tup[1])

         
    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)

        if self.hash_arr[idx]:
            found = False
            for i in range(len(self.hash_arr[idx])):
                if self.hash_arr[idx][i][0] == key:
                    self.hash_arr[idx][i] = (key, value)
                    found = True
            if not found:
                self.hash_arr[idx].append((key, value))

        else:
            self.hash_arr[idx].append((key, value))
            self.size += 1
        
        if self.size / self.capacity > 0.75:
            self._rehash()


    def get(self, key: int) -> int:
        idx = self._hash(key)
        if not self.hash_arr[idx]:
            return -1
        
        for k, v in self.hash_arr[idx]:
            if k == key:
                return v
        
        return -1
        


    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if not self.hash_arr[idx]:
            return None
        
        self.hash_arr[idx] = []
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)