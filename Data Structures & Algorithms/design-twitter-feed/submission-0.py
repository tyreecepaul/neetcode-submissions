import heapq

import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.users = {}   # followerId -> set(followeeIds)
        self.tweets = {}  # userId -> [[time, tweetId]]

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.time -= 1
        self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        followees = self.users.get(userId, set()).copy()
        followees.add(userId)  # include own tweets temporarily

        for followeeId in followees:
            if followeeId in self.tweets and self.tweets[followeeId]:
                idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][idx]

                # heap entry:
                # [time, tweetId, followeeId, next_index]
                heapq.heappush(
                    minHeap,
                    [time, tweetId, followeeId, idx - 1]
                )

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)

            res.append(tweetId)

            if idx >= 0:
                next_time, next_tweetId = self.tweets[followeeId][idx]

                heapq.heappush(
                    minHeap,
                    [next_time, next_tweetId, followeeId, idx - 1]
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = set()

        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
