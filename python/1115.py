# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:50:21 2020

@author: AlvinChen
"""
import threading as th
class FooBar:
    def __init__(self, n):
        self.n = n
        self.f=th.Semaphore(1)
        self.b=th.Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            self.f.acquire()
            printFoo()
            self.b.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):

            # printBar() outputs "bar". Do not change or remove this line.
            self.b.acquire()
            printBar()
            self.f.release()
