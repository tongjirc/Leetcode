# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:40 2020

@author: AlvinChen
"""
class Solution:
    def isPalindrome(self, s):
        """
        input type:str
        output type:bool
        """
        Length=len(s)
        s=s.lower()
        start,end=0,len(s)-1
        while end>=start:
            while start<Length and not (57>=ord(s[start])>=48 or 122>=ord(s[start])>=97 or ord(s[start])==32 ):
#                print("start",s[start])
                start+=1
            while end>=0 and not (57>=ord(s[end])>=48 or 122>=ord(s[end])>=97 or ord(s[end])==32):
#                print("end",s[end])
                end-=1
            if  not (start<Length or end>=0) or s[end]!=s[start]:return False
            start,end=start+1,end-1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True

if __name__=="__main__":
    try:
        a=Solution()
        str1= input()
        print(a.isPalindrome(str1))
    except Exception as e:
        print(e)