# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:51:44 2020

@author: AlvinChen
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    def lowestCommonAncestor(self, initial, p, q):
        """
        input type: TreeNode, TreeNode, TreeNode
        output type: TreeNode
        beyond time limit
        """
        def bfs():
            bfslst = [initial]
            num = 0
            finishlst = []
            qploc = []
            while bfslst:
                root = bfslst.pop(0)
                if not root:
                    finishlst.append(root)
                    bfslst.append(None)
                    bfslst.append(None)
                else:
                    finishlst.append(root)
                    bfslst.append(root.left)
                    bfslst.append(root.right)
                    if root.val == p.val or root.val == q.val:
                        num += 1
                        qploc.append(len(finishlst)-1)
                        if num == 2:
                            break
            while qploc[0] != qploc[1]:
                if qploc[0] > qploc[1]:
                    qploc[0] //= 2
                else:
                    qploc[1] //= 2

            return finishlst[qploc[0]]
        return bfs()


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return  # 1.
        if not left:
            return right  # 3.
        if not right:
            return left  # 4.
        return root  # 2. if left and right:


if __name__ == "__main__":
    try:
        a = Solution()
        nums, target = eval(input()), eval(input())
        print(a.lowestCommonAncestor(nums, target))
    except Exception as e:
        print(e)
