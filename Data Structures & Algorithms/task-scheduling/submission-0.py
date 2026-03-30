from _heapq import heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [cnt * - 1 for cnt in counter.values()]
        q = deque()
        heapq.heapify(max_heap)
        time = 0

        while max_heap or q:
            time += 1
            
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                item = q.popleft()
                heapq.heappush(max_heap, item[0])
        
        return time

                


            

        
        return count
