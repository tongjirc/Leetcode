# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:23:42 2020

@author: AlvinChen
"""

class Solution1:
    """
    down to up beyond time limit
    """
    def jump(self, steps):
        N=len(steps)
        prelst=[]
        dplst=[[i,steps[i]+i,i] for i in range(N)]
        def findminstep(n,targetlst):
            reachablelst=[]
            if n>0:targetlst.append(n-1)
            for i in targetlst:
                if dplst[i][1]>=n:
                    reachablelst.append(i)
            if reachablelst:return([min([dplst[i][2] for i in reachablelst])+1,reachablelst])
            else:return ([inf,[]])
        for i in range(N):
            minstep,prelst=findminstep(i,prelst)
            dplst[i][2]=min(minstep,dplst[i][2])
        return dplst[N-1][2]

class Solution:
    """
    down to up beyond time limit
    """
    def jump(self, steps):
        now,cnt=0,0
        length=len(steps)
        while(now <length -1):
            max,maxind=0,0
            for i in range(steps[now],0,-1):
                if now+i==length-1:
                    maxind=length-1
                    break
                if i+now<length and now+steps[i+now]+i>max:
                    max=now+steps[i+now]+i
                    maxind=now+i
            now=maxind
            cnt+=1
        return cnt

if __name__=="__main__":
    s=Solution()
    steps=eval(input())
    print(s.jump(steps))

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