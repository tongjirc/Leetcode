# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:57:42 2020

@author: AlvinChen
"""
class Solution1:
    def lengthOfLongestSubstring(self, chlst):
        """
        input type: string
        output type: int
        """
        num=[]
        start,end=0,0
        if not chlst:return len(num)
        for i in range(len(chlst)):
            key=chlst[start:end].find(chlst[i])
            if key!=-1:
                start=key+start+1
                end+=1
            else:
                end+=1
            num.append(end-start)
        return max(num)


class Solution:
    def lengthOfLongestSubstring(self, chlst):
        """
        input type: string
        output type: int
        """
        nummax,length=0,len(chlst)
        start,end=0,0
        if not chlst:return nummax
        for i in range(len(chlst)):
            key=chlst[start:end].find(chlst[i])
            if key!=-1 or i==length-1:
                if end-start>nummax or i==length-1:
                    end+=1
                    nummax=end-start
                start=key+start+1
                end+=1
            else:
                end+=1
        return nummax

if __name__=="__main__":
    try:
        a=Solution()
        chlst= input()
        print(a.lengthOfLongestSubstring(chlst))
    except Exception as e:
        print(e)