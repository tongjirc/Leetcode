# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 0:02:21 2020

@author: AlvinChen
"""

import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        length=0
        dictChar=collections.Counter(s)
        for i in dictChar.keys():
            length+=int(dictChar[i]/2)*2
        if length<len(s):
            length+=1
        return length


if __name__=="__main__":
	s=Solution()
	words=eval(input())
	chars=eval(input())
	print(s.longestPalindrome(words,chars))
