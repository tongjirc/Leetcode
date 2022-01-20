# Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。 
# 
#  给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，
# 返回 false 。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# 输出：true
# 解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。 
# 
#  示例 2： 
# 
#  
# 输入：hand = [1,2,3,4,5], groupSize = 4
# 输出：false
# 解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hand.length <= 10⁴ 
#  0 <= hand[i] <= 10⁹ 
#  1 <= groupSize <= hand.length 
#  
# 
#  
# 
#  注意：此题目与 1296 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-
# consecutive-numbers/ 
#  Related Topics 贪心 数组 哈希表 排序 👍 162 👎 0


from functools import reduce
from itertools import product

# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if groupSize == 1: return True
        minus_item = collections.deque()  # num,minus_time
        count = collections.Counter(hand)
        pre_key = None
        for key in sorted(count.keys()):
            if len(minus_item) != 0 and pre_key != None and key != pre_key + 1:
                return False
            for _ in range(len(minus_item)):
                item = minus_item.popleft()
                count[key] -= item[0]
                if item[1] <= 1:
                    continue
                else:
                    item[1] -= 1
                    minus_item.append(item)
            pre_key = key
            if count[key] < 0:
                return False
            elif count[key] == 0:
                continue
            else:
                minus_item.append([count[key], groupSize - 1])
                count[key] = 0
        return True if len(minus_item) == 0 else False


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(so.isNStraightHand(hand, groupSize))
print(True)

hand = [1, 2, 3, 4, 5]
roupSize = 4
print(so.isNStraightHand(hand, groupSize))
print(False)
