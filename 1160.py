# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:01:21 2020

@author: AlvinChen
"""
import collections

class Solution:
    def countCharacters(self, words, chars):
        allc=collections.Counter(chars)
        nums=0
        for word in words:
            keys=collections.Counter(word)
            for i,j in zip(keys.keys(),keys.values()):
                if j>allc[i]:
                    break
            else:
                nums+=len(word)
        return nums


if __name__=="__main__":
	s=Solution()
	words=eval(input())
	chars=eval(input())
	print(s.countCharacters(words,chars))
