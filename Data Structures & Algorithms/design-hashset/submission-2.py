class MyHashSet:

    def __init__(self):
        self.capacity = 100
        self.size = 0
        self.hash_arr = [[] for x in range(self.capacity)]
    
    def _hash(self, key):
        return key % self.capacity

    def _rehash(self):
        old_arr = self.hash_arr
        self.capacity = self.capacity * 2
        self.size = 0
        self.hash_arr = [[] for x in range(self.capacity)]

        for bucket in old_arr:
            for k in bucket:
                self.add(k)


    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        idx = self._hash(key)
        self.hash_arr[idx].append(key)
        self.size += 1

        if self.size / self.capacity > 0.75:
            self._rehash()


    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for item in self.hash_arr[idx]:
            if item == key:
                self.hash_arr[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.hash_arr[idx]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)