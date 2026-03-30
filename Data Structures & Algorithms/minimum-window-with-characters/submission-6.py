class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        counter_window = defaultdict(int)
        counterT = defaultdict(int)
        min_heap = []
        heapq.heapify(min_heap)
        
        for ch in t:
            counterT[ch] += 1
        
        l = 0
        r = 0

        while r < len(s):
            counter_window = Counter(s[l:r + 1])            
            is_good = True
            for k, v in counterT.items():
                if k not in counter_window or counter_window[k] < v:
                    is_good = False
                    break
            
            if not is_good:
                r += 1
                
            else:
                heapq.heappush(min_heap, (r + 1 - l, s[l: r + 1]))
                l += 1
        if min_heap:   
            return heapq.heappop(min_heap)[1]
        return ""
        