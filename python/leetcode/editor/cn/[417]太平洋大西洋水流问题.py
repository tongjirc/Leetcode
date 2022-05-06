# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。 
# 
#  这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上
# 单元格 高于海平面的高度 。 
# 
#  岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。 
# 
#  返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可
# 流向大西洋 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入: heights = [[2,1],[1,2]]
# 输出: [[0,0],[0,1],[1,0],[1,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == heights.length 
#  n == heights[r].length 
#  1 <= m, n <= 200 
#  0 <= heights[r][c] <= 10⁵ 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 449 👎 0


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


import time
from functools import reduce
from itertools import product
from memory_profiler import profile


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        rt_lst = []
        # pacific Ocean
        lst_label_pacific = [[0 for _ in range(n)] for _ in range(m)]
        lst_label_atlantic = [[0 for _ in range(n)] for _ in range(m)]
        lst_multi_bfs_pacific = collections.deque()
        lst_multi_bfs_atlantic = collections.deque()
        for i in range(n):
            lst_multi_bfs_pacific.append([0, i])
            lst_multi_bfs_atlantic.append([m - 1, i])
        for i in range(m):
            lst_multi_bfs_pacific.append([i, 0])
            lst_multi_bfs_atlantic.append([i, n - 1])

        while lst_multi_bfs_pacific:
            x, y = lst_multi_bfs_pacific.popleft()
            lst_label_pacific[x][y] = 1
            for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                x1, y1 = x + i, y + j
                if 0 <= x1 < m and 0 <= y1 < n and lst_label_pacific[x1][y1] != 1 and heights[x1][y1] >= heights[x][y]:
                    lst_multi_bfs_pacific.append([x1, y1])

        while lst_multi_bfs_atlantic:
            x, y = lst_multi_bfs_atlantic.popleft()
            if lst_label_atlantic[x][y] == 1:
                continue
            lst_label_atlantic[x][y] = 1
            if lst_label_pacific[x][y] == 1:
                rt_lst.append([x, y])
            for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                x1, y1 = x + i, y + j
                if 0 <= x1 < m and 0 <= y1 < n and lst_label_atlantic[x1][y1] != 1 and heights[x1][y1] >= heights[x][y]:
                    lst_multi_bfs_atlantic.append([x1, y1])

        return rt_lst


# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(so.pacificAtlantic(heights))
    print([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])


@profile(precision=8)
def speed_memory_test():
    print("\nSpeed and memory test")
    start = time.time()
    so = Solution()
    for _ in range(10000):
        pass
    print("Spend time:" + str(int((time.time() - start) * 1000)) + "ms")


# end test

def test():
    precesion_test()
    speed_memory_test()


if __name__ == "__main__":
    test()
