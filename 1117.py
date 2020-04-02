# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:01:11 2020

@author: AlvinChen
"""
class H2O:
    def __init__(self):
        self.h, self.o = [], []

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.append(releaseHydrogen)
        self.res()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.append(releaseOxygen)
        self.res()

    def res(self):
        if len(self.h) > 1 and len(self.o) > 0:
            self.h.pop(0)()
            self.h.pop(0)()
            self.o.pop(0)()

if __name__=="__main__":
	s=Solution()
	island=eval(input())
	print(s.maxDistance(island))
