# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:08:43 2020

@author: AlvinChen
"""
class Solution1:
    def translateNum(self, num):
        """
        input type:int
        output type:int
        """
        num=str(num)
        Length=len(num)
        dp=[0]*(Length+1)
        dp[0],dp[1]=1,1
        for i in range(2,Length+1):
            if "10"<=num[i-2:i]<="25":
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        return dp[-1]

class Solution:
    def translateNum(self, num):
        """
        input type:int
        output type:int
        """
        num=str(num)
        Length=len(num)
        pree,pre=1,1
        for i in range(2,Length+1):
            if "10"<=num[i-2:i]<="25":
                now=pre+pree
            else:
                now=pre
            pree=pre
            pre=now
        return now

if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.translateNum(nums))

