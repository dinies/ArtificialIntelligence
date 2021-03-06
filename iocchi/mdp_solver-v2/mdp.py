# Basic functions for MDP planning and learning
# Luca Iocchi 2015

import sys
import random
 
# Domain independent functions

def valueIteration(X,A,P,r,gamma=0.9,iterations=10,Sxf=[]):
    V={}
    for x in X:
        V[x]=0
    
    for i in range(iterations):
        print "\nIteration ",i
        Vn = dict(V) # clone
        for x1 in X: # current state
          if (not x1 in Sxf):
            #print "\tCurrent state ",x1
            maxVa=-1
            for a in A:
                #print "\t\tAction ",a
                sumx=0
                for x2 in X: # next state
                    #print "\t\t\tSuccessor state ",x2," prob: ",P(x1,a,x2)
                    sumx += P(x1,a,x2) * (r(x1,a,x2) + gamma * V[x2])
                maxVa = max(sumx,maxVa)
            Vn[x1] = maxVa
        V = Vn
        print "V  = ",V
        #print "pi = ",optimalPolicy(V)
    return V

# compute optimal policy from the value function V
def optimalPolicyV(V,X,A,P,r,gamma=0.9):
    pi = {}
    bestA = []  # set of best actions
    for x1 in X:
        maxVa=-1
        for a in A:
            sumx=0
            for x2 in X: # next state
                sumx += P(x1,a,x2) * (r(x1,a,x2) + gamma * V[x2])
            if sumx>maxVa:
               maxVa = sumx
               bestA = [a]
            elif sumx==maxVa:
               bestA = bestA + [a]
        pi[x1] = random.choice(bestA) # choose one among the best actions for state x
    return pi


def getQ(Q,x,a):
    if Q.has_key((x,a)):
        return Q[(x,a)]
    else:
        return 0
      
# deterministic Q update
def updateQdet(Qn,Q,A,x1,a,x2,r,gamma):
    maxQ=-1
    for a2 in A:
        maxQ=max(getQ(Q,x2,a2),maxQ)
    Qn[(x1,a)] = r + gamma * maxQ

    
visits = {}

# non-deterministic Q update 
def updateQ(Qn,Q,A,x1,a,x2,r,gamma,alpha):
    global visits
    if (alpha<0):
        if (not visits.has_key((x1,a))):
            visits[(x1,a)] = 0
        alpha = 1.0 / (1.0 + visits[(x1,a)])
        visits[(x1,a)] = visits[(x1,a)] + 1            
    maxQ=-1
    for a2 in A:
        maxQ=max(getQ(Q,x2,a2),maxQ)
    Qn[(x1,a)] = getQ(Q,x1,a) + alpha * (r + gamma*maxQ - getQ(Q,x1,a))


def argmaxQa(Q,x,A):
    maxQ=-1
    bestA=[]
    for a in A:
        q = getQ(Q,x,a)
        if q>maxQ:
            maxQ = q
            bestA = [a] # set of best actions for state x
        elif q==maxQ:   
            bestA = bestA + [a]
    return random.choice(bestA)

def chooseA(Q,x,A,epsilon):
    # epsilon greedy
    a=A[0]
    if random.random()<epsilon:
        a = random.choice(A)
        print "Exploration"
    else:        
        a = argmaxQa(Q,x,A)
        print "Exploitation"
    return a

    
# x0: initial state
# Sxf: set of final states
# A: set of actions
# delta_exec(x,a): execution function to observe the successor state 
#                  of executing a from x
# reward_exec(x,a): reward function to observe the reward obtained  
#                   by executing a from x
# gamma: discount factor
# epsilon: value for epsilon-greedy strategy
# alpha: value for non-deterministic update rule
# iterations: number of iterations of the algorithm
# RR: [output] cumulative reward obtained over iterations
# NA: [output] total number of actions executed 
def Qlearning(x0,Sxf,A,delta_exec,reward_exec,gamma,  epsilon,alpha,iterations,RR,NA):
    Q = {}
    x = x0
    NA[0] = 0
    for i in range(iterations):
        Qn = dict(Q)
        print "\nIteration ",i
        x = x0 # set current state as initial state
        g = 1.0 # discount
        rr = 0.0 # cumulative reward
        while (not x in Sxf):
            a = chooseA(Q,x,A,epsilon)
            # Execution of action a in state x
            print " - Execution: state ",x," action ",a
            NA[0] = NA[0] + 1
            x2 = delta_exec(x,a)
            r = reward_exec(x,a,x2)
            rr = rr + r * g
            g = g * gamma
            print " - Outcome: state ",x2," reward ",r
            if x2==-1:
                break
            updateQ(Qn,Q,A,x,a,x2,r,gamma,alpha)
            x = x2
        Q = Qn
        RR[i] = rr
        print "Cumulative reward: ",rr
        print "\n"
    return Q


# Compute the optimal policy from the Q function
def optimalPolicyQ(Q,X,A):
    pi = {}
    for x in X:
        # set best action for state x
        pi[x] = argmaxQa(Q,x,A)
    return pi

    
# Execute policy pi from x0 to Sxf, print execution trace and cumulative reward
def execTrace(x0,xg,Sxf,delta,r,gamma,pi):
    print "Execution trace from ",x0
    i=0
    x=x0
    g = 1.0
    rr = 0.0 # cumulative reward
    while (not x in Sxf):
        a = pi[x]
        i=i+1
        x2 = delta(x,a)
        r2 = r(x,a,x2)
        print i,":  ",x,a,"->",x2," ",r2
        rr = rr + r2*g
        g = g*gamma
        x = x2
        if (x<0):
            print "Execution Error"
            return
        if (i==10):
            print "LOOP"
            return
    if x==xg:
        print "GOAL"
    else:
        print "FAIL"
    print "Cumulative reward = ",rr
