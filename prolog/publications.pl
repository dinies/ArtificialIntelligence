publication(nardi, brachman).
publication(brachman, erdos).
publication(einstein, erdos).
publication(konolige, erdos).
publication(september, nardi).

distance(X,1) :- publication(X,erdos).
distance(X,N) :- publication(X,W), distance(W,N1), N is N1 + 1.