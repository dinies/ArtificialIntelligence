contained(irina, natasha).
contained(natasha,olga).
contained(olga,katarina).

in(X,Y) :- contained(X,Y).
in(X,Y) :- contained(X,Z), in(Z,Y).
