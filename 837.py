# -*- coding: utf-8 -*-
"""
Created on Jun  3 17:11:54 2020

@author: AlvinChen
"""

class Solution1:
    def new21Game(self, N, K, W) -> float:
        """
        input type: int, int, int
        output type:float
        """
        if N<K:return 0
        pos=[1]+[0]*N
        for i in range(0,N+1):
            if i==K:
                return sum(pos)
            for j in range(i+1,min(N+1,i+1+W)):pos[j]+=pos[i]/W
            pos[i]=0

class Solution:
    def new21Game(self, N, K, W) -> float:
        """
        input type: int, int, int
        output type:float
        """
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]

if __name__=="__main__":
    try:
        a=Solution()
        b=Solution1()
#        N, K, W= eval(input()),eval(input()),eval(input())
        N, K, W=100,17,1000
        print(a.new21Game(N, K, W))
        print(b.new21Game(N, K, W))
    except Exception as e:
        print(e)