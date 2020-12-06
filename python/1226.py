# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:55:14 2020

@author: AlvinChen
"""
import threading

class DiningPhilosophers:

    def __init__(self):
        self.l = threading.Lock()

    def wantsToEat(self, philosopher, *actions):
        self.l.acquire()
        [*map(lambda func: func(), actions)]
        self.l.release()
