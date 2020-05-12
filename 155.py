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


    def push(self, x: int) -> None:


    def pop(self) -> None:


    def top(self) -> int:


    def getMin(self) -> int:



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