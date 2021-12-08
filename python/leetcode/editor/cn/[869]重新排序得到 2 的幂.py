# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。 
# 
#  如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：1
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：10
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：16
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：24
# 输出：false
#  
# 
#  示例 5： 
# 
#  输入：46
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10^9 
#  
#  Related Topics 数学 计数 枚举 排序 👍 111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set_n=collections.Counter(list(str(n)))
        for i in range(33):
            set_tmp=collections.Counter(list(str(2**i)))
            if set_n==set_tmp:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
so=Solution()
n=1521
print(so.reorderedPowerOf2(n))