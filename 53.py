# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:48:05 2020

@author: AlvinChen
"""

class Solution:
    def maxSubArray(self,nums):
        """
        input: List[int]
        output:int
        """
        if not nums:return 0
        length,f=len(nums),[nums[0]]
        for i in range(1,length):
            f.append(max(nums[i]+f[-1],nums[i]))
        return max(f)



if __name__=="__main__":
    try:
        a=Solution()
        nums= eval(input())
        print(a.maxSubArray(nums))
    except Exception as e:
        print(e)