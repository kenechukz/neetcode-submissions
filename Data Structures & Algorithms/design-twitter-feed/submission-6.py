class Twitter:
    import heapq

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        user_and_following = {userId} | self.following[userId]
        heap = []
        for uid in user_and_following:
            if self.tweets[uid]:
                time, tweet_id = self.tweets[uid][-1]
                idx = len(self.tweets[uid]) -1
                heapq.heappush(heap, (time, tweet_id, uid, idx))
                
        feed = []
        while heap and len(feed) < 10:
            time, tweetId, uid, idx = heapq.heappop(heap)
            feed.append(tweetId)

            if idx - 1 >= 0:
                next_time, next_tweet = self.tweets[uid][idx -1]
                heapq.heappush(heap, (next_time, next_tweet, uid, idx-1))

        return feed


            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

        
        


"""
R:
we have twiiter class


void postTweet(int userId, int tweetId) - unique tweet each time for user userId

List<Integer> getNewsFeed(int userId) -  10 most recent tweets which includes userId's tweets and 
people they follow

- needs to dynamic update with regards to who user follows

void follow(int followerId, int followeeId) The user with ID followerId follows followeeID

void unfollow(int followerId, int followeeId) The user with ID followerId unfollows followeeID

t
tweets[userID] = [tweetID1, tweetID2]

tweets[userID2] = [tweetID3, tweetID4]

tweets = [tweetID1, tweetID2, tweetID3, (userID2,tweetID4)]

following[userID] = {userID2, userID3}

10 most recent from

E:
1 <= userId, followerId, followeeId <= 100
0 <= tweetId <= 1000






"""