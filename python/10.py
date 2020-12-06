# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:19:07 2020

@author: AlvinChen
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s and len(p) == 1: return False

        nrow = len(s) + 1
        ncol = len(p) + 1

        dp = [[False for c in range(ncol)] for r in range(nrow)]

        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, ncol):
            j = c-1
            if p[j] == '*': dp[0][c] = dp[0][c-2]

        for r in range(1, nrow):
            i = r-1
            for c in range(1, ncol):
                j = c-1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r-1][c-1]
                elif p[j] == '*':
                    if p[j-1] == s[i] or p[j-1] == '.':
                        dp[r][c] = dp[r-1][c] or dp[r][c-2]
                    else:
                        dp[r][c] = dp[r][c-2]
                else:
                    dp[r][c] = False

        return dp[nrow-1][ncol-1]


if __name__=="__main__":
    try:
        a=Solution()
        height= eval(input())
        print(a.maxArea(height))
    except Exception as e:
        print(e)