# 在一个 10⁶ x 10⁶ 的网格中，每个网格上方格的坐标为 (x, y) 。 
# 
#  现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表
# ，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。 
# 
#  每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。 
# 
#  只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
# 无法向北或者向东移动是因为方格禁止通行。
# 无法向南或者向西移动是因为不能走出网格。 
# 
#  示例 2： 
# 
#  
# 输入：blocked = [], source = [0,0], target = [999999,999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= blocked.length <= 200 
#  blocked[i].length == 2 
#  0 <= xi, yi < 10⁶ 
#  source.length == target.length == 2 
#  0 <= sx, sy, tx, ty < 10⁶ 
#  source != target 
#  题目数据保证 source 和 target 不在封锁列表内 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 哈希表 👍 89 👎 0


from functools import reduce
from itertools import product

# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """

        def Manhattan(x, y):
            return abs(target[0] - x) + abs(target[1] - y)

        # A star
        pq = []
        matrix = [[0 for i in range(1000000)] for i in range(1000000)]
        for block in blocked:
            matrix[block[0]][block[1]] = -1
        heapq.heappush(pq, [0 + Manhattan(source[0], source[1]), 0, source])
        while pq:
            _, f, node = heapq.heappop(pq)
            if node == target:
                return True
            else:
                matrix[node[0]][node[1]] = 1
            for i, j in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                x, y = node[0] + i, node[1] + j
                if 1000000 > x >= 0 and 1000000 > y >= 0 and matrix[x][y] == 0:
                    heapq.heappush(pq, [f + 1 + Manhattan(x, y), f + 1, [x, y]])
        return False


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
blocked = []
source = [0, 0]
target = [1, 1]
print(so.isEscapePossible(blocked, source, target))
