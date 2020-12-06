# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:16:57 2020

@author: AlvinChen
"""

#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import math
class Solution:
    def rightSideView(self, root):
        lst={}
        def bfs(nlst):
            """
            bfs
            """
            while nlst:
                nroot,n=nlst.pop(0)
                if nroot:
                    lst[n]=nroot.val
                    nlst.append([nroot.left,n+1])
                    nlst.append([nroot.right,n+1])
        bfs([[root,0]])
        return(list(lst.values()))



if __name__=="__main__":
    try:
        a=Solution()
        root= eval(input())
        print(a.rightSideView(root))
    except Exception as e:
        print(e)