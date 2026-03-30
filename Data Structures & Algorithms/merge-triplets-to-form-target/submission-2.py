class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_first = float("-inf")
        max_second = float("-inf")
        max_third = float("-inf")

        for triplet in triplets:
            if (
                triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2] 
            ):
                continue


            max_first = max(max_first, triplet[0])
            max_second = max(max_second, triplet[1])
            max_third = max(max_third, triplet[2])
        
        max_triplet = [max_first, max_second, max_third]
        
        return max_triplet == target