# Alice 和 Bob 再次设计了一款新的石子游戏。现有一行 n 个石子，每个石子都有一个关联的数字表示它的价值。给你一个整数数组 stones ，其中 
# stones[i] 是第 i 个石子的价值。 
# 
#  Alice 和 Bob 轮流进行自己的回合，Alice 先手。每一回合，玩家需要从 stones 中移除任一石子。 
# 
#  
#  如果玩家移除石子后，导致 所有已移除石子 的价值 总和 可以被 3 整除，那么该玩家就 输掉游戏 。 
#  如果不满足上一条，且移除后没有任何剩余的石子，那么 Bob 将会直接获胜（即便是在 Alice 的回合）。 
#  
# 
#  假设两位玩家均采用 最佳 决策。如果 Alice 获胜，返回 true ；如果 Bob 获胜，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：stones = [2,1]
# 输出：true
# 解释：游戏进行如下：
# - 回合 1：Alice 可以移除任意一个石子。
# - 回合 2：Bob 移除剩下的石子。 
# 已移除的石子的值总和为 1 + 2 = 3 且可以被 3 整除。因此，Bob 输，Alice 获胜。
#  
# 
#  示例 2： 
# 
#  
# 输入：stones = [2]
# 输出：false
# 解释：Alice 会移除唯一一个石子，已移除石子的值总和为 2 。 
# 由于所有石子都已移除，且值总和无法被 3 整除，Bob 获胜。
#  
# 
#  示例 3： 
# 
#  
# 输入：stones = [5,1,2,4,3]
# 输出：false
# 解释：Bob 总会获胜。其中一种可能的游戏进行方式如下：
# - 回合 1：Alice 可以移除值为 1 的第 2 个石子。已移除石子值总和为 1 。
# - 回合 2：Bob 可以移除值为 3 的第 5 个石子。已移除石子值总和为 = 1 + 3 = 4 。
# - 回合 3：Alices 可以移除值为 4 的第 4 个石子。已移除石子值总和为 = 1 + 3 + 4 = 8 。
# - 回合 4：Bob 可以移除值为 2 的第 3 个石子。已移除石子值总和为 = 1 + 3 + 4 + 2 = 10.
# - 回合 5：Alice 可以移除值为 5 的第 1 个石子。已移除石子值总和为 = 1 + 3 + 4 + 2 + 5 = 15.
# Alice 输掉游戏，因为已移除石子值总和（15）可以被 3 整除，Bob 获胜。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 10⁵ 
#  1 <= stones[i] <= 10⁴ 
#  
#  Related Topics 贪心 数组 数学 计数 博弈 👍 48 👎 0


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
from functools import lru_cache


class Solution(object):

    def stoneGameIX(self, stones):
        """
        : type stones: List[int]
        : rtype: bool
        """

        # @lru_cache()
        def simulate(stones_now, num_discard_stone, alice_turn):
            """
            判断当前alice是否可以赢
            """
            if stones_now is []: return False
            for i in range(len(stones_now)):
                if (num_discard_stone + stones_now[i]) % 3 == 0:
                    continue
                else:
                    alice_win = simulate(stones_now[:i] + stones_now[i + 1:], num_discard_stone + stones_now[i],
                                         not alice_turn)
                    if alice_win and alice_turn:
                        return True
                    elif not alice_win and not alice_turn:
                        return False
                    else:
                        continue
            return False if alice_turn else True

        return simulate(stones, 0, True)


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
stones = [5, 1, 2, 4, 3]
print(so.stoneGameIX(stones))
print(False)

stones = [2, 1]
print(so.stoneGameIX(stones))
print(True)

stones = [5, 1, 2, 4, 3]
print(so.stoneGameIX(stones))
print(False)
