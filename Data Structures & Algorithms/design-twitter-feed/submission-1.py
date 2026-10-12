
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        # Include the user's own tweets
        users = self.following[userId] | {userId}

        # Add the newest tweet from each followed user
        for uid in users:
            tweets = self.tweets[uid]

            if tweets:
                index = len(tweets) - 1
                timestamp, tweetId = tweets[index]

                heapq.heappush(
                    heap, (-timestamp, tweetId, uid, index)
                )

        feed = []

        # Extract the 10 most recent tweets
        while heap and len(feed) < 10:
            _, tweetId, uid, index = heapq.heappop(heap)
            feed.append(tweetId)

            # Add this user's next older tweet
            index -= 1

            if index >= 0:
                timestamp, nextTweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-timestamp, nextTweetId, uid, index)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
