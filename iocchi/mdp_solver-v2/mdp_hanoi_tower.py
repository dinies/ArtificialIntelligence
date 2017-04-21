# MDP for Hanoi tower
# Luca Iocchi 2015

import sys

import mdp
from mdp import *

# MDP definition for Hanoi tower problem

D = ['D1', 'D2', 'D3']  # three disks D(i+1) bigger than Di

# S = { 'P1': {...}, 'P2': {...}, 'P3': ... }  
# three poles with list of disks (first = top)

S = [
 { 'P1': ['D1','D2','D3'], 'P2': [], 'P3': [] }, # S1 = initial state
 { 'P1': ['D2','D3'], 'P2': ['D1'], 'P3': [] }, # S2 
 { 'P1': ['D2','D3'], 'P2': [], 'P3': ['D1'] }, # S3 
 { 'P1': ['D3'], 'P2': ['D1'], 'P3': ['D2'] }, # S4 
 { 'P1': ['D3'], 'P2': ['D2'], 'P3': ['D1'] }, # S5 
 { 'P1': ['D3'], 'P2': [], 'P3': ['D1','D2'] }, # S6 
 { 'P1': ['D3'], 'P2': ['D1','D2'], 'P3': [] }, # S7 
 { 'P1': [], 'P2': ['D3'], 'P3': ['D1','D2'] }, # S8
 { 'P1': [], 'P2': ['D1','D2'], 'P3': ['D3'] }, # S9
 { 'P1': ['D1'], 'P2': ['D3'], 'P3': ['D2'] }, # S10
 { 'P1': [], 'P2': ['D1','D3'], 'P3': ['D2'] }, # S11
 { 'P1': [], 'P2': ['D2'], 'P3': ['D1','D3'] }, # S12
 { 'P1': ['D2'], 'P2': [], 'P3': ['D1','D3'] }, # S13
 { 'P1': ['D1'], 'P2': ['D2'], 'P3': ['D3'] }, # S14
 { 'P1': [], 'P2': ['D2'], 'P3': ['D1','D3'] }, # S15
 { 'P1': ['D1'], 'P2': [], 'P3': ['D2','D3'] }, # S16
 { 'P1': [], 'P2': [], 'P3': ['D1','D2','D3'] } # S17 = goal state
]

# Encoding of the states
X = range(0,len(S))

A = [ ('P1','P2'), ('P2','P1'), ('P1','P3'), ('P3','P1'), ('P2','P3'), ('P3','P2') ]

x0 = 0 # initial state
xg = 16 # goal state
Sxf = [xg]

def deltaS(s, a):
    pfrom=a[0]
    pto=a[1]
    if (len(s[pfrom])==0 or s==S[xg]):
        return 0
    s2 = dict(s) # clone
    d = s[pfrom][0]
    s2[pfrom] = s[pfrom][1:len(s[pfrom])]
    s2[pto] =  [d] + s2[pto]
    return s2

def delta(x, a):
    s=S[x]
    s2 = deltaS(s,a)
    if (s2 in S):
        x2 = S.index(s2)
        return x2
    else:
        return -1

        
def delta_exec(x, a):
    x2 = delta(x,a)
    if x2!=-1:
        return x2
    else:
        return x

        
def P(x1,a,x2): # transition probability
    if delta(x1,a)==x2:
        return 1
    else:
        return 0


def r(x1,a,x2): # reward value
    if x2==xg:
        return 100
    else:
        return 0



# main
# Options: [Planning/Learning] [niterations] [epsilon] [alpha]

niter=10
gamma=0.9
epsilon=0.5
alpha=1.0
mode='Planning'
if (len(sys.argv)>1):
    mode=sys.argv[1]
if (len(sys.argv)>2):
    niter=int(sys.argv[2])
if (len(sys.argv)>3):
    epsilon=float(sys.argv[3])

if mode=='Planning':
    V = valueIteration(X,A,P,r,gamma,niter,Sxf)
    pi = optimalPolicyV(V,X,A,P,r,gamma)
    print "Optimal policy: ",pi
    execTrace(x0,xg,Sxf,delta,r,gamma,pi)
else:
    RR = range(niter)
    NA = [0]
    Q = Qlearning(x0,Sxf,A,delta_exec,r,gamma,epsilon,alpha,niter,RR,NA)
    print "Q = ",Q
    pi = optimalPolicyQ(Q,X,A)
    print "Cumulative reward = ",RR
    print "Total actions executed = ",NA[0]
    print "Optimal policy: ",pi
    execTrace(x0,xg,Sxf,delta,r,gamma,pi)

