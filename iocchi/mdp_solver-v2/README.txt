Python MDP solver (Luca Iocchi, 2015)
-------------------------------------

* mdp.py contains basic domain independent functions for planning and learning with MDP.

* mdp_<problem>.py contains the definition of a particular MDP problem.

How to use

$ python mdp_<problem>.py <Planning|Learning> <n. iterations> <epsilon>

<epsilon>=0.0 -> exploitation
<epsilon>=1.0 -> exploration

Example:

$ python mdp_grid.py Planning 10

Notes:

$ python mdp_grid.py Learning 7  
sometimes fails

$ python mdp_grid2.py Learning 8  
fails/not optimal/optimal

grid2 with reward at node 'I'=10 -> optimal solution = shortest path
grid2 with reward at node 'I'=30 -> optimal solution = longest path



$ python mdp_hanoi_tower.py Learning 8

may bring to non-optimal policy (R=47.8 instead of 53.1)

$ python mdp_hanoi_tower.py Learning 8 0.0
Action executed =   600-1200
Not always optimal policy

$ python mdp_hanoi_tower.py Learning 8 1.0
Action executed =  2000-4000
Optimal policy


Reward plot

$ python mdp_hanoi_tower.py Learning 30 0.1
$ python mdp_hanoi_tower.py Learning 30 0.5
$ python mdp_hanoi_tower.py Learning 30 0.9

Always found optimal policy, but reward is low when exploration (i.e., epsilon) is high


mdp_kbandit.py Learning 1

only one trial

mdp_kbandit.py Learning 2

the best of two trials (note sometimes, exploitation prevents different trials)

...

mdp_kbandit.py Learning 1000

average of all trials for each action

