class Solution:
    def are_connected(self, word1, word2):
        diff = 0
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
        
        return diff == 1

        

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        n = len(wordList)
        graph = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                word1 = wordList[i]
                word2 = wordList[j]
                
                if self.are_connected(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        queue = deque([beginWord])
        visited = set()
        res = []
        count = 0
        while queue:
            n = len(queue)
            count += 1
            for _ in range(n):
                node = queue.popleft()
                visited.add(node)
                res.append(node)
                if node == endWord:
                    print(res)
                    return count

                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            
        
        return 0


            
            
