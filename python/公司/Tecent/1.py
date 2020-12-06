# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:44:40 2020

@author: AlvinChen
"""

class Solution2:
    def findMedianSortedArrays(self):
        nums1,nums2= eval(input()),eval(input())
        midnum,one2two,i,mid=len(nums1)+(len(nums2)-len(nums1))//2,(len(nums1)%2+len(nums2)%2+1)%2,0,0
        while nums1 and nums2 and i<=midnum:
            if nums1[0]>nums2[0]:
                now=nums2.pop(0)
            else:
                now=nums1.pop(0)
            if i==midnum or i==midnum-one2two:
                mid+=now
            i+=1
        else:
            if i<=midnum and nums1:
                while i<=midnum:
                    now=nums1.pop(0)
                    if i==midnum or i==midnum-one2two:
                        mid+=now
                    i+=1
            elif i<=midnum and nums2:
                while i<=midnum:
                    now=nums2.pop(0)
                    if i==midnum or i==midnum-one2two:
                        mid+=now
                    i+=1
            if one2two:return mid/2
            else:return mid

class Solution:
    def longestPalindrome(self):
        """
        beyond time limit
        """
        s= input()
        if not s :return s
        length=len(s)

        def isreverse(start,end):
            while end!=start and end>start:
                if s[end]!=s[start]:return False
                else:start,end=start+1,end-1
            else:return True

        for maxl in range(length,0,-1):
            for i in range(0,length-maxl+1):
                if isreverse(i,i+maxl-1):return s[i:i+maxl]




if __name__=="__main__":
    try:
        a=Solution()
        print(a.longestPalindrome())
    except Exception as e:
        print(e)