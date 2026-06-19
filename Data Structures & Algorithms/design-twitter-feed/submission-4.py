class Twitter:
    def __init__(self):
        self.follows = {} # Follower id: set(followees ids)
        self.tweets = []
        self.SIZE = 10
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = set()
        if userId in self.follows:
            followees = self.follows[userId] 

        feed = []
        for tweet, uid in self.tweets[::-1]:
            if len(feed) >= self.SIZE:
                break
            
            if uid in followees or uid == userId:
                feed.append(tweet)
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set([followeeId])
        else:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return None
        
        if followeeId not in self.follows[followerId]:
            return None

        self.follows[followerId].remove(followeeId)