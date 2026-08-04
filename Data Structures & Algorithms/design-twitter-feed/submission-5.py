class Twitter:

    def __init__(self):
        self.tweet_count = defaultdict(int)
        self.tweet_repo = []
        self.following = defaultdict(set)


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_repo.append((userId, tweetId))
        self.tweet_count[userId] +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets_count = self.tweet_count[userId] 
        tweets = []
        
        for followee in self.following[userId]:
             all_tweets_count += self.tweet_count[followee]

        valid_no_tweets = min(10, all_tweets_count)


        for user, tweet in reversed(self.tweet_repo):
            if len(tweets) >= valid_no_tweets:
                break

            if user == userId or user in self.following[userId]:
                tweets.append(tweet)


        return tweets


            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        
        


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