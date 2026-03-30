class MyHashSet:

    def __init__(self):
        self.capacity = 100
        self.hash_arr = [[] for x in range(self.capacity)]
        

    def add(self, key: int) -> None:
        idx = key % self.capacity
        if key not in self.hash_arr[idx]:
            self.hash_arr[idx].append(key)


    def remove(self, key: int) -> None:
        idx = key % self.capacity
        for item in self.hash_arr[idx]:
            if item == key:
                print("will delete key", key, "at idx", idx)
                print(self.hash_arr[idx])
                self.hash_arr[idx].remove(key)
                print(self.hash_arr[idx])
        

    def contains(self, key: int) -> bool:
        idx = key % self.capacity
        for item in self.hash_arr[idx]:
            if item == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)