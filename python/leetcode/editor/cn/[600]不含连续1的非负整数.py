import numpy
import math
import collections

# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。
# 
#  示例 1: 
# 
#  输入: 5
# 输出: 5
# 解释: 
# 下面是带有相应二进制表示的非负整数<= 5：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。 
# 
#  说明: 1 <= n <= 10⁹ 
#  Related Topics 动态规划 👍 153 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findIntegers(self, n):
        numOfChoice1={}
        def findNIntegers(maximum, num1, first):
            # first: 1/0
            sumChoice=0
            if num1<=0:return 0
            if num1==1 and first==0:return 1
            elif first and 2**(num1-1)>maximum:return 0
            elif first and 2**num1-1<=maximum:
                if numOfChoice1.get(num1):sumChoice=numOfChoice1.get(num1)
                else:
                    pre=[0,1]
                    for i in range(1,num1):
                        pre=[pre[0]+pre[1],pre[0]]
                        if numOfChoice1.get(num1):


                    numOfChoice1[num1]=sumChoice
                    sumChoice=sum(pre)
            else:
                if first==1:
                    sumChoice+=findNIntegers(maximum-2**(num1-1),num1-1,0)
                else:
                    sumChoice+=findNIntegers(maximum,num1-1,1)
                    sumChoice+=findNIntegers(maximum,num1-1,0)
            # print(sumChoice,num1,first)
            return sumChoice
        num=int(math.log(n,2))+1
        n1=findNIntegers(n,num,0)
        # print(n,num,0,n1)
        n1+=findNIntegers(n,num,1)
        # print(n-2*(num-1),num,1,n1)
        return n1
# leetcode submit region end(Prohibit modification and deletion)
so=Solution()
print(so.findIntegers(8))