import time

class Twitter:

    def __init__(self):
        self.follows = defaultdict(list)
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.users:
            self.users[userId]["posts"].append((tweetId, time.time())) 
        else:
            self.users[userId] = {"posts": [(tweetId, time.time())]} 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.follows[userId] + [userId]
        posts = []
        for userId in following:
            if userId in self.users:
                posts.extend(self.users[userId]["posts"])
        posts.sort(key=lambda x: x[1], reverse=True)
        
        return [x[0] for x in posts[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId] and followeeId != followerId:
            self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

        
