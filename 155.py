# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:14:33 2020

@author: AlvinChen
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst=[]
        self.orderlst=[]
        self.length=0
        return

    def push(self, x: int) -> None:
        if not self.length: self.orderlst.append(x)
        else:
            i=self.length-1
            while i>=0 and self.orderlst[i]<=x:
                i-=1
            self.orderlst.insert(i+1,x)
        self.lst.append(x)
        self.length+=1
        return

    def pop(self) -> None:
        if not self.length: return
        self.orderlst.remove(self.lst.pop())
        self.length-=1
        return


    def top(self) -> int:
        return self.lst[-1] if self.length else None


    def getMin(self) -> int:
        return self.orderlst[-1] if self.length else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.mergeKLists(n))
    except Exception as e:
        print(e)