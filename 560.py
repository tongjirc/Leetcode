# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:39:01 2020

@author: AlvinChen
"""
class Solution1:
    def subarraySum(self, nums,k):
        num=0
        length=len(nums)
        for i in range(length):
            for j in range(i+1,length+1):
                if sum(nums[i:j])==k:num+=1
        return num

class Solution2:
    def subarraySum(self, nums,k):
        num=0
        length=len(nums)
        for i in range(length):
            s=0
            for j in range(i,length):
                s=s+nums[j]
                if s==k:num+=1
        return num

class Solution3:
    def subarraySum(self, nums: List[int], k: int) -> int:
      cnt, n =  0, len(nums)
      pre = [0] * (n + 1)
      for i in range(1, n + 1):
          pre[i] = pre[i - 1] + nums[i - 1]
      for i in range(1, n + 1):
          for j in range(i, n + 1):
              if (pre[j] - pre[i - 1] == k): cnt += 1
      return cnt

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        acc = count = 0
        for num in nums:
            acc += num
            if acc == k:
                count += 1
            if acc - k in d:
                count += d[acc-k]
            if acc in d:
                d[acc] += 1
            else:
                d[acc] = 1
        return count


if __name__=="__main__":
    try:
        a=Solution()
        nums,k= eval(input()),eval(input())
        print(a.subarraySum(nums,k))
    except Exception as e:
        print(e)