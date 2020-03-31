# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:02:43 2020

@author: AlvinChen
"""
class Circle1():
    def __init__(self,n):
        self.Lst=list(range(0,n))
    def cur(self):
        return self.Lst[0]
    def roll(self):
        self.Lst.append(self.Lst.pop(0))
    def out(self):
        self.Lst.pop(0)
    def length(self):
        return len(self.Lst)

class Solution1:
    def lastRemaining(self, n, m):
        c=Circle1(n)
        for i in range(n-1):
            for j in range(m-1):
                c.roll()
            c.out()
        return c.cur()


class Solution:
    """
    时间复杂度：O(n)，需要求解的函数值有 n 个。
    空间复杂度：O(1)，只使用常数个变量。
    """
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f

if __name__=="__main__":
	s=Solution()
	arr=eval(input())
	k=eval(input())
	print(s.lastRemaining(arr,k))
