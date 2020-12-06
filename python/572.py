# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:52:00 2020

@author: AlvinChen
"""
# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def isSubtree(self, s, t):
        bfsLst=[s]
        def bfs():
            while bfsLst:
                Node=bfsLst.pop(0)
                if isequal(Node,t):return True
                if Node.left:bfsLst.append(Node.left)
                if Node.right:bfsLst.append(Node.right)
            else:return False

        def isequal(Node1,t):
            eqlst=[(Node1,t)]
            while eqlst:
                now,target=eqlst.pop(0)
                if now.val!=target.val:return False
                if  (now.left != 0) ^ (target.left != 0):return False
                if (now.right != 0) ^ (target.right != 0):return False
                if now.left: eqlst.append((now.left,target.left))
                if now.right: eqlst.append((now.right,target.right))
            else:return True

        return bfs()

if __name__=="__main__":
    try:
        a=Solution()
        height= eval(input())
        print(a.isSubtree(height))
    except Exception as e:
        print(e)