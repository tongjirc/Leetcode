# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 0:01:21 2020

@author: AlvinChen
"""
class Solution:
    bits=[]
    length=0
    def go(self,i):
        if i>self.length-1:
            return False
        if i==self.length-1 and self.bits[i]==0:
            return True
        if self.bits[i]==1:
            return self.go(i+2)
        else:
            return self.go(i+1)
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        self.bits=bits
        self.length=len(bits)
        if bits:
            return self.go(0) 
        else:
            return False


if __name__=="__main__":
	s=Solution()
	words=eval(input())
	chars=eval(input())
	print(s.countCharacters(words,chars))
