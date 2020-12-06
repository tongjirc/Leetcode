# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:22:49 2020

@author: AlvinChen
"""
import collections

import threading as th
class Foo:
    def __init__(self):
        self.one=th.Semaphore(1)
        self.two=th.Semaphore(0)
        self.three=th.Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        self.one.acquire()
        printFirst()
        self.two.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        self.two.acquire()
        printSecond()
        self.three.release()


    def third(self, printThird: 'Callable[[], None]') -> None:

        # printThird() outputs "third". Do not change or remove this line.
        self.three.acquire()
        printThird()
        self.one.release()
