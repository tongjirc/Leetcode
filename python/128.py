# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:38:20 2020

@author: AlvinChen
"""
class Solution1:
    def longestConsecutive(self, nums) :
        """
        没考虑重复情况
        input: List[int]
        output:-> int
        """
        if not nums:return 0
        maxl=1
        Length=len(nums)
        nums.sort()
        start=0
        for end in range(Length):
            if nums[end]-nums[start]==end-start:
                if end-start+1>maxl:maxl=end-start+1
            else:
                start=end
            if end==Length:break
        return maxl

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__=="__main__":
    s=Solution()
    steps=eval(input())
    print(s.canJump(steps))