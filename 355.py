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
        wholelst=[]
        if userId in self.user:
            for i in self.user[userId]:
                if i in self.twit:
                    if len(self.twit[i])<=10:
                        wholelst.extend(self.twit[i])
                    else:
                        wholelst.extend(self.twit[i][0:10])
        if userId in self.twit:
            if len(self.twit[userId])<=10:
                wholelst.extend(self.twit[userId])
            else:
                wholelst.extend(self.twit[userId][0:10])
        wholelst=sorted(wholelst,key=lambda x:x[1],reverse=True)
        return [wholelst[i][0] for i in range(0,min(len(wholelst),10))]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
            if followerId in self.user.keys() and followeeId not in self.user[followerId]:
                self.user[followerId].append(followeeId)
            else:
                self.user[followerId]=[(followeeId)]


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.user.keys() and followeeId in self.user[followerId]:
            self.user[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
if __name__=="__main__":
    obj = Twitter()
    obj.postTweet(1,5)
    param_2 = obj.getNewsFeed(1)
    obj.follow(1,2)
    obj.postTweet(2,6)
    obj.postTweet(2,2)
    obj.postTweet(2,4)
    param_2 = obj.getNewsFeed(1)
    obj.unfollow(1,2)
    param_2 = obj.getNewsFeed(1)