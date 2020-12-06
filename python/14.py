# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:19:07 2020

@author: AlvinChen
"""
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        str1=""
        l1,l2=len(strs),len(min(strs,key=lambda x:len(x)))
        for i in range(l2):
            s=strs[0][i]
            for i in range(l1):
                if strs[i]!=s:
                    return str1
            else:
                str1+=s
        return str1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        strl=0
        l1,l2=len(strs),len(min(strs,key=lambda x:len(x)))
        for i in range(l2):
            s=strs[0][i]
            for j in range(l1):
                if strs[j][i]!=s:
                    return strs[0][0:strl]
            else:
                strl+=1
        return strs[0][0:strl]

if __name__=="__main__":
    try:
        a=Solution()
        height= eval(input())
        print(a.maxArea(height))
    except Exception as e:
        print(e)