# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:59:27 2020

@author: AlvinChen
"""

#class Solution:
#    def reverseWords(self, s):
#        slst=s.strip().split(" ")
#        slst.reverse()
#        sclean=[i for i in slst if not (" "  in i or not i)]
#        newstr=" ".join(sclean)
#        return newstr

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

if __name__=="__main__":
    try:
        s=Solution()
        s=input()
        print(s.reverseWords(s))
    except Exception as e:
        print(e)