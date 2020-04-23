# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:52:29 2020

@author: AlvinChen
"""
"25 13,10 4,61 73,15 6.20 9"
class Solution1:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod

class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7

        ans = 0
        for i in range(n // 25 + 1):
            rest = n - i * 25
            a, b = rest // 10, rest % 10 // 5
            ans += (a + 1) * (a + b + 1)
        return ans % mod

if __name__=="__main__":
	s=Solution()
	n=eval(input())
	print(s.waysToChange(n))
