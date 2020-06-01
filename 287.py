# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:23:42 2020

@author: AlvinChen
"""
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        sn,snn=1,nums[0]
        length=len(nums)
        for i in range(1,length-1):
            sn^=i+1
        for i in range(1,length):
            snn^=nums[i]
        return snn^sn

import collections
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        c=collections.Counter(nums)
        return sorted(c.items(),key=lambda x:x[1])[-1][0]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            # 此时重复元素一定出现在 [1, 4] 区间里

            if cnt > mid:
                # 重复的元素一定出现在 [left, mid] 区间里
                right = mid
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid + 1, right]
                left = mid + 1
        return left

if __name__=="__main__":
    s=Solution()
    steps=eval(input())
    print(s.canJump(steps))