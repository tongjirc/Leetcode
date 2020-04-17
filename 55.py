# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:23:42 2020

@author: AlvinChen
"""
import time
class Solution1:
    """
    set method Beyond the time limit
    """
    def canJump(self, steps):
        Can=False
        N=len(steps)
        canlst=set([0])
        for i in range(N):
            if i not in canlst:
                continue
            else:
                lst=list(map(lambda x: x+i,range(1,steps[i]+1)))
                canlst=canlst.union(set(lst))
        if N-1 in canlst:
            Can=True
        return Can

class Solution2:
    """
    up to down Beyond the time limit
    """
    def canJump(self, steps):
        reachlst=[0]
        def reachable(N):
            if N in reachlst:
                return True
            for i in range(N-1,-1,-1):
                if steps[i]>=N-i:
                    if reachable(i):
                        reachlst.append(N)
                        return True
                    else:
                        continue
            else:
                return False
        return reachable(len(steps)-1)

class Solution3:
    """
    down to up Beyond the time limit
    """
    def canJump(self, steps):
        notreachlst=[]
        length=len(steps)
        def reachable(N):
            if N in notreachlst:return False
            if steps[N]+N>=length-1:return True
            for i in range(steps[N]+1,0,-1):
                if reachable(N+i):return True
                else:continue
            else:
                notreachlst.append(N)
                return False
        return reachable(0)

class Solution:
    """
    down to up Beyond the time limit
    """
    def canJump(self, steps):
        maxlenght=0
        length=len(steps)
        for i in range(length):
            if i>maxlenght:return False
            else:maxlenght=max(maxlenght,i+steps[i])
        return True

if __name__=="__main__":
    s=Solution()
    steps=eval(input())
    print(s.canJump(steps))

#    s2=Solution2()
#    steps=[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
#    start=time.time()
#    for i in range(10000):
#        s.canJump(steps)
#    print(time.time()-start)
#    start1=time.time()
#    for i in range(10000):
#        s2.canJump(steps)
#    print(time.time()-start1)