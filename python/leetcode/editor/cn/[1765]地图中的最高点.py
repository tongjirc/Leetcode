# 给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。 
# 
#  
#  如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。 
#  如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。 
#  
# 
#  你需要按照如下规则给每个单元格安排高度： 
# 
#  
#  每个格子的高度都必须是非负的。 
#  如果一个格子是是 水域 ，那么它的高度必须为 0 。 
#  任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边） 
#  
# 
#  找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。 
# 
#  请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个
#  。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：isWater = [[0,1],[0,0]]
# 输出：[[1,0],[2,1]]
# 解释：上图展示了给各个格子安排的高度。
# 蓝色格子是水域格，绿色格子是陆地格。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
# 输出：[[1,1,0],[0,1,1],[1,2,2]]
# 解释：所有安排方案中，最高可行高度为 2 。
# 任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == isWater.length 
#  n == isWater[i].length 
#  1 <= m, n <= 1000 
#  isWater[i][j] 要么是 0 ，要么是 1 。 
#  至少有 1 个水域格子。 
#  
#  Related Topics 广度优先搜索 数组 矩阵 👍 33 👎 0


def Lst2ListNode(Lst):
    dummy = ListNode(-1, None)
    rcd = dummy
    for i in Lst:
        nd = ListNode(i, None)
        dummy.next = nd
        dummy = dummy.next
    return rcd.next


def ListNode2Lst(node):
    Lst = []
    while node:
        Lst.append(node.val)
        node = node.next
    return Lst


class ListNode(object):
    _name = "ListNode"

    def __init__(self, val=0, next=None, lst=[]):
        if not lst:
            self.val = val
            self.next = next
        else:
            self.val = lst.pop(0)
            if lst:
                self.next = ListNode(lst=lst)
            else:
                self.next = None

    def __str__(self):
        return str(ListNode2Lst(self))


class TreeNode:
    def __init__(self):
        self.id = None
        self.left = None
        self.right = None


from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        search_lst = []
        SEARCHED = 1000
        l1, l2 = len(isWater), len(isWater[0])
        max_height = 0
        isWaterCopy = [[0 for _ in range(l2)] for _ in range(l1)]

        def search_build(point, own, plus):
            """
            plus == False: 将 非own 置为 -height 并放入 search_lst，将 own 置为 searched,
            plus == True:  将 非own 置为 own - 1 并放入 search_lst, 将 own 置为 searched
            """
            for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x, y = point[0] + i, point[1] + j
                if l1 > x >= 0 and l2 > y >= 0 and isWater[x][y] != SEARCHED and isWater[x][y] != own:
                    search_lst.append([[x, y], -1] if not plus else [[x, y], own - 1])
                    isWater[x][y] = -1 if not plus else own - 1
            isWater[point[0]][point[1]] = SEARCHED

        for i in range(l1):
            for j in range(l2):
                if isWater[i][j] == 1:
                    search_build([i, j], 1, False)
                    isWaterCopy[i][j] = 0

        while search_lst:
            node, own = search_lst.pop(0)
            max_height = max(max_height, -own)
            search_build(node, own, True)
            isWaterCopy[node[0]][node[1]] = -own

        return isWaterCopy

# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
isWater = [[0, 1], [0, 0]]
print(so.highestPeak(isWater))
print([[1, 0], [2, 1]])

print(so.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
print([[1, 1, 0], [0, 1, 1], [1, 2, 2]])
