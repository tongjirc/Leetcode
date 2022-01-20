# n 位格雷码序列 是一个由 2ⁿ 个整数组成的序列，其中：
#  
#  每个整数都在范围 [0, 2ⁿ - 1] 内（含 0 和 2ⁿ - 1） 
#  第一个整数是 0 
#  一个整数在序列中出现 不超过一次 
#  每对 相邻 整数的二进制表示 恰好一位不同 ，且 
#  第一个 和 最后一个 整数的二进制表示 恰好一位不同 
#  
# 
#  给你一个整数 n ，返回任一有效的 n 位格雷码序列 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：[0,1,3,2]
# 解释：
# [0,1,3,2] 的二进制表示是 [00,01,11,10] 。
# - 00 和 01 有一位不同
# - 01 和 11 有一位不同
# - 11 和 10 有一位不同
# - 10 和 00 有一位不同
# [0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
# - 00 和 10 有一位不同
# - 10 和 11 有一位不同
# - 11 和 01 有一位不同
# - 01 和 00 有一位不同
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 16 
#  
#  Related Topics 位运算 数学 回溯 👍 388 👎 0


from functools import reduce
from itertools import product
# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class Solution(object):
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
for n in range(1, 17):
    print(n)
    print(so.grayCode(n))

n = 1231248
start = time.time()
for i in range(100):
    _ = 2 ** n
cost1 = time.time() - start
print("1 cost:", cost1)
start = time.time()
for i in range(100):
    _ = (1 << n)
cost2 = time.time() - start
print("2 cost:", cost2)
print(cost1 / cost2)
