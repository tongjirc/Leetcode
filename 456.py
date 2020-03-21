# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:57:53 2020

@author: AlvinChen
"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_num = nums[0]
        min_list = []
        res = []
        for i in nums:
            if i <= min_num:
                min_list.append(i)
                min_num = i
            else:
                min_list.append(min_num)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                res.append(nums[i])
                continue
            try:
                while res[-1] <= min_list[i]:
                    del res[-1]
            except IndexError as e:
                res.append(nums[i])
                continue
            if nums[i] <= res[-1]:
                res.append(nums[i])
                continue
            else:
                return True
        return False




if __name__=="__main__":
	s=Solution()
	words=eval(input())
	print(s.find132pattern(words))
