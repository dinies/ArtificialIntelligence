
cousin(X,Y) :- parent(Z,X), parent(W,Y), siblings(W,Z), X\=Y.

father(daniele,michela).
father(daniele,jacopo).
father(eriberto,daniele).
father(antonio,eriberto).
father(sandro,lucio).

mother(alma,eriberto).
mother(annamaria,daniele).
mother(annamaria,marcello).
mother(annamaria,sandro).
son(X,Y) :- mother(Y,X).

son(X,Y) :- father(Y,X).

descendant(X,Y) :- son(X,Y).
descendant(X,Y) :- son(Z,Y), descendant(X,Z).
parent(P, X) :- father(P, X).
parent(P, X) :- mother(P, X).
siblings(X, Y) :- parent(Z, X), parent(Z, Y), X\=Y.

    auntuncle(X,Y) :- parent(Z,Y),siblings(X,Z).
    
%Define in PROLOG the relation onlychild(X), exploiting the family defined before.
sameLevelInTreeOP( X ,Y ):- parent( Z, X) , parent( Z,Y), !.
sameLevelInTreeOP( X ,Y ):- parent( W, X) , parent( Z,Y), W \= Z, sameLevelInTreeOP( W ,Z).
onlychildOP(X):- sameLevelInTreeOP(X ,W), not(siblings(X, W)).
