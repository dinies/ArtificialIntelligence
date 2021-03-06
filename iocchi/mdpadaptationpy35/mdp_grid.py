# MDP for non-deterministic grid example in AI book Chapters 17 and 21
# Luca Iocchi 2015

import sys
import random

import mdp
from mdp import *


# MDP definition for simple non-deterministic grid world

X = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'F', 'G']
A = ['R', 'L', 'U', 'D']

deltaS = {('S0','R'): ['S1'], ('S0','U'): ['S4'],
          ('S1','R'): ['S2'], ('S1','L'): ['S0'],
          ('S2','R'): ['S3'], ('S2','L'): ['S1'], ('S2','U'): ['S5'],
          ('S3','U'): ['F'],  ('S3','L'): ['S2'],
          ('S4','U'): ['S6'], ('S4','D'): ['S0'],
          ('S5','U'): ['S8'], ('S5','D'): ['S2'], ('S5','R'): ['F'],
          ('S6','R'): ['S7'], ('S6','D'): ['S4'],
          ('S7','R'): ['S8'], ('S7','L'): ['S6'],
          ('S8','R'): ['G'],  ('S8','L'): ['S7'],  ('S8','D'): ['S5']
        }

reward = { 'G': 100, 'F': -100 }

x0 = 'S0'
xg = 'G'
Sxf = ['G', 'F'] # final states

def delta(x, a):
    if deltaS.has_key((x,a)):
        return deltaS[(x,a)]
    else:
        return []


def P(x1,a,x2): # transition probability (general non-deterministic case)
    Sx2 = delta(x1,a)
    if (x2 in Sx2):
        if len(Sx2)==1:
            return 1
        else:
            return 1.0/len(Sx2)
    else:
        return 0

        
def r(x1,a,x2): # reward value
    if (deltaS.has_key((x1,a)) and reward.has_key(x2)):
        return reward[x2]
    else:
        return 0


def delta_exec(x,a):
    Sx2 = delta(x,a)
    if len(Sx2)==0:
        print "Execution error"
        return x
    else:
        return random.choice(Sx2)

        
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
if (len(sys.argv)>4):
    alpha=float(sys.argv[4])

if mode=='Planning':
    V = valueIteration(X,A,P,r,gamma,niter,Sxf)
    pi = optimalPolicyV(V,X,A,P,r,gamma)
    print "Optimal policy: ",pi
    execTrace(x0,xg,Sxf,delta_exec,r,gamma,pi)
else:
    RR = range(niter)
    NA = [0]
    Q = Qlearning(x0,Sxf,A,delta_exec,r,gamma,epsilon,alpha,niter,RR,NA)
    print "Q = ",Q
    pi = optimalPolicyQ(Q,X,A)
    print "Cumulative reward = ",RR
    print "Total action executed = ",NA[0]
    print "Optimal policy: ",pi
    execTrace(x0,xg,Sxf,delta_exec,r,gamma,pi)



