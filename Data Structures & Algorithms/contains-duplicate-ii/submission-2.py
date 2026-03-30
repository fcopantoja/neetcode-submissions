class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset = set()
        
        for i in range(len(nums)):
            if nums[i] in myset:
                return True
            
            myset.add(nums[i])
            

            if (i >= k):
                myset.remove(nums[i - k])
        
        return False


        