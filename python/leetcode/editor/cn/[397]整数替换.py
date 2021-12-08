# 给定一个正整数 n ，你可以做如下操作： 
# 
#  
#  如果 n 是偶数，则用 n / 2替换 n 。 
#  如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。 
#  
# 
#  n 变为 1 所需的最小替换次数是多少？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 4
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  Related Topics 贪心 位运算 记忆化搜索 动态规划 👍 139 👎 0
import collections
from functools import reduce
from itertools import product
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict_dp= {}
        lst_bfs=collections.deque()
        lst_bfs.append([n,0])
        while lst_bfs:
            num,depth=lst_bfs.popleft()
            print(num,depth)
            if dict_dp.get(num):
                continue
            elif num==1:
                return depth
            else:
                dict_dp[num]=depth
                if num%2==0:
                    #偶數
                    lst_bfs.append([num/2,depth+1])
                else:
                    #奇数
                    lst_bfs.append([num+1,depth+1])
                    lst_bfs.append([num-1,depth+1])
        return None
# leetcode submit region end(Prohibit modification and deletion)
so=Solution()
n=4
print(so.integerReplacement(n))