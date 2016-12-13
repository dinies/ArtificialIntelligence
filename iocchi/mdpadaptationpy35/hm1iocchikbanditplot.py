#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:19:45 2016

@author: edoardoghini
"""

# MDP for non-deterministic k-bandit problem
# Luca Iocchi 2016
#edited for local execution Dinies

import sys
import random
from random import gauss
from matplotlib import pyplot
import numpy as np
import mdp


# MDP definition 

X = ['S0','G']
A = ['a1', 'a2', 'a3', 'a4']

reward = { 'a1': [100,50], 'a2': [90,20], 'a3': [70,50], 'a4': [50,50] }

x0 = 'S0'
xg = 'G'
Sxf = ['G'] # final states


def delta(x, a):
    return 'G'


def P(x1,a,x2): # transition probability
    Sx2 = delta(x1,a)
    if (x2 in Sx2):
        if len(Sx2)==1:
            return 1
        else:
            return 1.0/len(Sx2)
    else:
        return 0

        
def r(x1,a,x2): # reward value
    return gauss(reward[a][0],reward[a][1])


def delta_exec(x,a):
    Sx2 = delta(x,a)
    if len(Sx2)==0:
        print ("Execution error" )
        return x
    else:
        return random.choice(Sx2)
        
        
# main
# Options: [niterations] [Planning/Learning] [epsilon] [alpha]
# Note: alpha < 0 -> computed as 1 / (1 + visits(x,a))
niter=100
gamma=0.9
epsilon=0.5
alpha=-1
mode='Learning'
if (len(sys.argv)>1):
    mode=sys.argv[1]
if (len(sys.argv)>2):
    niter=int(sys.argv[2])
if (len(sys.argv)>3):
    epsilon=float(sys.argv[3])
if (len(sys.argv)>4):
    alpha=float(sys.argv[4])

if mode=='Planning':
    V = mdp.valueIteration(X,A,P,r,gamma,niter,Sxf)
    pi = mdp.optimalPolicyV(V,X,A,P,r,gamma)
    print ("Optimal policy: ",pi)
    mdp.execTrace(x0,xg,Sxf,delta_exec,r,gamma,pi)
else:
    RR = list(range(niter))
    NA = [0]
    Q = mdp.Qlearning(x0,Sxf,A,delta_exec,r,gamma,epsilon,alpha,niter,RR,NA)
    print ("Q = ",Q)
    pi = mdp.optimalPolicyQ(Q,X,A)
    print ("Cumulative reward = ",RR)
    print ("Total action executed = ",NA[0])
    print ("Optimal policy: ",pi)
    mdp.execTrace(x0,xg,Sxf,delta_exec,r,gamma,pi)
    #plotting
    pyplot.figure()
    pyplot.plot(np.arange(1,101),RR)
    pyplot.title("Cumulative Reward")
    
    #first strategy k 30 iterations with greater mean value selection
    Q_results=[]
    for action in A:
        iterations = 30
        RR = list(range(iterations))
        NA = [0]
        singleton_action= [action]
        Q = mdp.Qlearning(x0,Sxf,singleton_action,delta_exec,r,gamma,epsilon,alpha,iterations,RR,NA)
        Q_results.append(Q)
    print(Q_results)


