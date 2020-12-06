# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:43:14 2020

@author: AlvinChen
"""
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=collections.Counter(nums)
        return list(a.keys())[list(a.values()).index(1)]