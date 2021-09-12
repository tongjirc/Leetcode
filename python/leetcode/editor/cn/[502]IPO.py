# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:09:38 2019

@author: AlvinChen
"""
"""
*******************************************************************"""

from random import random
from math import sin, asin, cos, radians, fabs, sqrt
from gurobipy import *
import logging
import pandas as pd
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import time
from sklearn.metrics import r2_score
from scipy.stats import norm

def optimize():
    print("*********************** MODEL 1 ***********************")
    m = Model('502')

    logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                        filename='dataAnalysis.log',
                        filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]'
                        # 日志格式
                        )
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    length = len(capital)

    wt_v = m.addVars(length, vtype=GRB.CONTINUOUS, name='wt')
    d_v=m.addVars(k,length,vtype=GRB.BINARY,name='d')

    p=profits
    c=capital

    #obj1 = quicksum((R[i]-Rm_v[i])*(R[i]-Rm_v[i]) for i in range(dM))
    obj1 = wt_v[k-1]
    #obj3 =quicksum(C_v[i] for i in range(dM))-np.shape(np.where(S<=3.2))[1]
    m.setObjective(obj1, GRB.MAXIMIZE)

    for i in range(k):
        if i!=0:
            m.addConstr(wt_v[i]==wt_v[i-1]+quicksum(p[j]*d_v[i,j] for j in range(length)),name="update")
        else:
            m.addConstr(wt_v[i]==w+quicksum(p[j]*d_v[i,j] for j in range(length)),name="update")
        if i!=k-1:
            m.addConstr(quicksum(d_v[i,j] for j in range(length))>=quicksum(d_v[i+1,j] for j in range(length)),name="jumpContinuely")
        m.addConstr(quicksum(d_v[i,j] for j in range(length))<=1,name="chooseOne")
        m.addConstr(wt_v[i]>=0,"wCons")
        if i!=0:
            for j in range(length):
                m.addConstr(d_v[i,j]*(wt_v[i-1]-c[j])>=0,name="capacityCons")
        else:
            for j in range(length):
                m.addConstr(d_v[i,j]*(w-c[j])>=0,name="capacityCons")

    for j in range(length):
        m.addConstr(quicksum(d_v[i,j] for i in range(k))<=1,name="chooseOneTime")


    m.setParam(GRB.Param.Threads, 4)
    #m.setParam(GRB.Param.MIPGap, 0.03)
    m.setParam(GRB.Param.TimeLimit, 10000)
    #m.setParam(GRB.Param.MIPFocus, 2) # 0 deflaut, 1 find fast feasibility, 2 fast prove the best
    #m.setParam(GRB.Param.FeasibilityTol, 0.01)
    m.update()
    m.optimize()

    if m.status == GRB.Status.OPTIMAL:  # m.getAttr('x', x_v).items()
        print("****************","Solution found!","****************")
        wa,d=[],[]
        for i in range(k):
            wa.append(wt_v[i].x)
            da=[]
            for j in range(length):
                da.append(d_v[i,j].x)
            d.append(da)
        wa=np.array(wa)
    else:
        print("****************","Solution not found!","****************")


if __name__=="__main__":
    optimize()