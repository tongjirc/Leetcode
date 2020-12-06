# -*- coding: utf-8 -*-
"""
Created on  Fri Mar 27 22:17:53 2020

@author: AlvinChen
"""
import collections
import math
class Solution:
    def hasGroupsSizeX(self, words):
        items=list(collections.Counter(words).values())
        minigcd=math.inf
        if len(items)<2:
            return False
        for i in range(len(items)-1):
            gcd=math.gcd(items[i],items[i+1])
            if gcd>=2 and minigcd==math.inf:
                minigcd=gcd
            elif gcd>=2:
                gcdgcd=math.gcd(minigcd,gcd)
                if gcdgcd>=2:
                    minigcd=gcdgcd
                else:
                    return False
            else:
                return False
        else:
            return True
        return False


        return Have

if __name__=="__main__":
	s=Solution()
	words=eval(input())
	print(s.hasGroupsSizeX(words))
