class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:        
        if len(hand) % groupSize:
            return False
        

        hand.sort()
        counts = defaultdict(int)

        for num in hand:
            counts[num] += 1
        
        for card in hand:
            if counts[card] > 0:
                for i in range(card, card + groupSize):
                    if not counts[i]:
                        return False
                    counts[i] -= 1
                
        return True
