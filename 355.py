# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:49:50 2020

@author: AlvinChen
"""

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user={}
        self.twit={}
        self.time=0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        """
        self.time+=1
        if userId in self.twit.keys():
            self.twit[userId].append((tweetId,self.time))
        else:
            self.twit[userId]=[(tweetId,self.time)]


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """




    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.user.keys():
            self.twit[followerId].append(followeeId)
        else:
            self.twit[followerId]=[(followeeId)]


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.user.keys() and followeeId in self.twit[followerId]:
            self.twit[followerId].remove(followeeId)
        else:
            return



# Your Twitter object will be instantiated and called as such:
if __name__=="__main__":
    obj = Twitter()
    obj.postTweet(1,5)
    param_2 = obj.getNewsFeed(1)
    obj.follow(1,2)
    obj.postTweet(2,6)
    param_2 = obj.getNewsFeed(1)
    obj.unfollow(1,2)
    param_2 = obj.getNewsFeed(1)