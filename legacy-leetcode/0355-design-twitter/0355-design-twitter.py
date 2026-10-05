from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        for author in self.following[userId] | {userId}:
            tweets = self.tweets[author]
            if tweets:
                index = len(tweets) - 1
                timestamp, tweet_id = tweets[index]
                heapq.heappush(heap, (timestamp, tweet_id, author, index))

        feed = []
        while heap and len(feed) < 10:
            _, tweet_id, author, index = heapq.heappop(heap)
            feed.append(tweet_id)

            index -= 1
            if index >= 0:
                timestamp, previous_tweet_id = self.tweets[author][index]
                heapq.heappush(
                    heap,
                    (timestamp, previous_tweet_id, author, index),
                )

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

- needs to dynamically update with regards to who user follows

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

if user tries follow themselves -> Do nothing


if user doesn't have a post yet and we follow them and try add their post to our feed

A:

for get newsfeed we intersect userId with all users they follow and add all most recent tweets for
each user to a heap with their time to help order the heap

when we add a tweet to our feed, if that users has more tweets we push those to the heap with the idx it corresponds
to in the tweets[userId x] array

we do this while heap exists and we have less than 10 tweets in our feed

this allows us to a time complexity of k log n

where k is the number of tweets for that users feed and n is the number of users (user + following)






"""
