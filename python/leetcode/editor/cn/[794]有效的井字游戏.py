# 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。 
# 
#  井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。 
# 
#  以下是井字游戏的规则： 
# 
#  
#  玩家轮流将字符放入空位（' '）中。 
#  玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。 
#  'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。 
#  当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。 
#  当所有位置非空时，也算为游戏结束。 
#  如果游戏结束，玩家不允许再放置字符。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = ["O  ","   ","   "]
# 输出：false
# 解释：玩家 1 总是放字符 "X" 。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = ["XOX"," X ","   "]
# 输出：false
# 解释：玩家应该轮流放字符。 
# 
#  示例 3： 
# 
#  
# 输入：board = ["XXX","   ","OOO"]
# 输出：false
#  
# 
#  Example 4: 
# 
#  
# 输入：board = ["XOX","O O","XOX"]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  board.length == 3 
#  board[i].length == 3 
#  board[i][j] 为 'X'、'O' 或 ' ' 
#  
#  Related Topics 数组 字符串 👍 55 👎 0


from functools import reduce
from itertools import product
# leetcode submit region begin(Prohibit modification and deletion)
import numpy as np
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        num_X, num_O = 0, 0
        lst_location_x = []
        lst_location_o = []
        accu_board = board[0] + board[1] + board[2]
        counter = collections.Counter(accu_board)

        def GameWin(word):
            if counter[word] >= 3:
                matrix = np.mat([list(i) for i in board])
                sum_slash = 0
                sum_op_slash = 0
                for i in range(3):
                    if sum(sum(matrix[:, i] == word)) == 3 or sum(sum(matrix[i, :] == word)) == 3:
                        return True
                    if matrix[i, i] == word:
                        sum_slash += 1
                    if matrix[i, 2 - i] == word:
                        sum_op_slash += 1
                if sum_slash == 3 or sum_op_slash == 3:
                    return True
                return False
            else:
                return False

        # 检查游戏游戏结束
        win_O = GameWin('O')
        win_X = GameWin('X')
        # 检查数量规则
        if not (counter['O'] == counter['X'] or counter['O'] + 1 == counter['X']) or (
                counter['O'] == counter['X'] and win_X) or (win_O and win_X) or (
                counter['O'] + 1 == counter['X'] and win_O):
            return False
        else:
            return True


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
board = ["XXO", "XOX", "OXO"]
print(so.validTicTacToe(board))