# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:40 2020

@author: AlvinChen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs_sum(self, root):
        """
        input: TreeNode
        output: type: -> int
        """
        if root == None: return 0
        val = root.val
        sum_l = max(0, self.dfs_sum(root.left))
        sum_r = max(0, self.dfs_sum(root.right))
        self.ans = max(self.ans, sum_l + sum_r + val)
        return  max(sum_l , sum_r) + val

    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = - 1e9
        self.dfs_sum(root)
        return self.ans


if __name__=="__main__":
    try:
        a=Solution()
        str1= input()
        print(a.isPalindrome(str1))
    except Exception as e:
        print(e)