prefix5([],_Ys).
prefix5([X|Xs],[X|Ys]) :- prefix5(Xs,Ys).