# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:23:42 2020

@author: AlvinChen
"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        outdic={}

        def bfs(root):
            bfslst=[(root,1)]
            nb=0
            while bfslst:
                root,n=bfslst.pop(0)
                if nb!=n:outdic.setdefault(n,[]).append(root.val)
                else:outdic[n].append(root.val)
                if root.left:bfslst.append((root.left,n+1))
                if root.right:bfslst.append((root.right,n+1))
                nb=n

        def dfs(root):
            dfslst=[(root,1)]
            while dfslst:
                root,n=dfslst.pop()
                outdic.setdefault(n,[]).append(root.val)
                if root.right:dfslst.append((root.right,n+1))
                if root.left:dfslst.append((root.left,n+1))

        if root: bfs(root)
        return list(outdic.values())



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