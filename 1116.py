# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:55:14 2020

@author: AlvinChen
"""
import threading as th
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z=th.Semaphore(1)
        self.e=th.Semaphore(0)
        self.o=th.Semaphore(0)

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,2*self.n+1):
            if i%2==1:
                self.z.acquire()
                printNumber(0)
            elif i%4==0:
                self.e.release()
            else:
                self.o.release()


    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,2*self.n+1):
            if i%4==0:
                self.e.acquire()
                printNumber(i//2)
                self.z.release()
            else:
                pass



    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,2*self.n+1):
            if i%4==2:
                self.o.acquire()
                printNumber(i//2)
                self.z.release()
            else:
                pass
