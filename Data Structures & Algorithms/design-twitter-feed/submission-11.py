import time

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId)) 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId] | {userId}
        heap = []
        res = []
        for userId in users:
            if userId in self.tweets:
                time, tweet_id = self.tweets[userId][-1]
                heapq.heappush(heap, (-time, tweet_id, userId, len(self.tweets[userId]) - 1))
        
        while heap and len(res) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx - 1 >= 0:
                next_time, next_tweetId = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-next_time, next_tweetId, u, idx - 1))
            
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

        
