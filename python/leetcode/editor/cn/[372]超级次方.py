# 你的任务是计算 aᵇ 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：a = 2, b = [3]
# 输出：8
#  
# 
#  示例 2： 
# 
#  
# 输入：a = 2, b = [1,0]
# 输出：1024
#  
# 
#  示例 3： 
# 
#  
# 输入：a = 1, b = [4,3,3,8,5,2]
# 输出：1
#  
# 
#  示例 4： 
# 
#  
# 输入：a = 2147483647, b = [2,0,0]
# 输出：1198
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a <= 2³¹ - 1 
#  1 <= b.length <= 2000 
#  0 <= b[i] <= 9 
#  b 不含前导 0 
#  
#  Related Topics 数学 分治 👍 188 👎 0


from functools import reduce
from itertools import product
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD=1337
        ans=1
        length=len(b)
        for k in range(0,length):
            ans=(((ans**10)%MOD)*((a**b[k])%MOD))%MOD
            print(reduce(lambda x,y:x*10+y,b[:k+1]),(a**reduce(lambda x,y:x*10+y,b[:k+1])%MOD),ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

so=Solution()
a=2
b=[4,3,3,8,5,2] #100
print(so.superPow(a,b))