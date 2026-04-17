class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_ships(capacity: int) -> int:
            ships = 1
            curr_capacity = capacity
            for weight in weights:
                if curr_capacity - weight < 0:
                    ships += 1
                    curr_capacity = capacity
                curr_capacity -= weight
            return ships
        res = sum(weights)

        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2
            
            ships = get_ships(mid)
            print(mid, ships)
            if ships <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res