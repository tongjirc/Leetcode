# -*- coding: utf-8 -*-
"""
Created on Tue May 5 22:59:30 2020

@author: AlvinChen
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, initroot):
        """
        input type: TreeNode
        output type: bool
        """
        def isValid(root,head=float(inf),tail=float(-inf)):
            if root==None:return True
            if tail<root.val<head and isValid(root.left,head=root.val) and isValid(root.right,tail=root.val):return True
            else:return False

        return isValid(initroot)



if __name__=="__main__":
    try:
        a=Solution()
        print(a.isValidBST())
    except Exception as e:
        print(e)