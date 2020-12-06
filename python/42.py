# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:50:27 2020

@author: AlvinChen
"""
class Solution1:
    def trap(self, height):
        if not height:
            return 0
        MaxH=max(height)
        everyrow=[]
        num=0
        for i in range(1,MaxH+1):
            row=""
            for j in range(len(height)):
                if height[j]>=i:
                    row+="1"
                else:
                    row+="0"
            everyrow.append(row)
        for lst in everyrow:
            left=lst.find("1")
            right=lst.rfind("1")
            if left==right:
                break
            else:
                for k in lst[left+1:right]:
                    if k=="0":
                        num+=1
        return num

import collections
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # 同时从左往右和从右往左计算有效面积
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n - i - 1] > max2:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        # 积水面积 = S1 + S2 - 矩形面积 - 柱子面积
        res = s1 + s2 - max1 * len(height) - sum(height)
        return res

class Solution(object):
    "求出最高点，然后依次向左遍历，向右遍历"
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        num=0
        if not height:
            return num
        maxind=height.index(max(height))
        clheight=height[:maxind+1]
        crheight=height[maxind:]
        #right search
        maxind=0
        while maxind!=len(crheight)-1:
            nextheight=max(crheight[maxind+1:])
            nextmaxind=crheight[maxind+1:].index(nextheight)+maxind+1
            w,l=nextmaxind-maxind-1,nextheight
            abstract=0
            for i in crheight[maxind+1:nextmaxind]:
                abstract+=i
            num=num+w*l-abstract
            maxind=nextmaxind
        #left search
        maxind=len(clheight)-1
        while maxind!=0:
            nextheight=max(clheight[:maxind])
            nextmaxind=clheight[:maxind].index(nextheight)
            w,l=maxind-nextmaxind-1,nextheight
            abstract=0
            for i in clheight[nextmaxind+1:maxind]:
                abstract+=i
            num=num+w*l-abstract
            maxind=nextmaxind
        return num

if __name__=="__main__":
    try:
        a=Solution()
        height= eval(input())
        print(a.trap(height))
    except Exception as e:
        print(e)