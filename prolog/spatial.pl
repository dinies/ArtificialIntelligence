on(glass,paper).
on(paper,disk).
left(pen,paper).
left(paper,apple).
right(apple,paper).
right(paper,pen).
front(bottle,paper).
front(paper,ring).
behind(ring,paper).
behind(paper,bottle).
below(disk,paper).
below(paper,glass).



isRight(X,Y) :- right(X,Y).
isRight(X,Y) :- right(X,Z), isRight(Z,Y).
isLeft(X,Y) :- left(X,Y).
isLeft(X,Y) :- left(X,Z) , isLeft(Z,Y).

isFront(X,Y) :- front(X,Y).
isFront(X,Y) :- front(X,Z), isFront(Z,Y).
isBehind(X,Y) :- behind(X,Y).
isBehind(X,Y) :- behind(Z,Y), isBehind(X,Z).

isOn(X,Y) :- on(X,Y).
isOn(X,Y) :- on(Z,Y), isOn(X,Z). 
isBelow(X,Y) :- below(X,Y).
isBelow(X,Y) :- below(X,Z), isBelow(Z,Y).

between(X,Y,Z) :- isOn(Y,X), isBelow(Z,X), format('~w is between ~w and ~w', [X,Y,Z]).
between(X,Y,Z) :- isOn(Z,X), isBelow(Y,X), format('~w is between ~w and ~w', [X,Y,Z]).

between(X,Y,Z) :- isFront(Y,X), isBehind(Z,X), format('~w is between ~w and ~w', [X,Y,Z]).
between(X,Y,Z) :- isFront(Z,X), isBehind(Y,X), format('~w is between ~w and ~w', [X,Y,Z]).

between(X,Y,Z) :- isRight(Y,X), isLeft(Z,X), format('~w is between ~w and ~w', [X,Y,Z]).
between(X,Y,Z) :- isRight(Z,X), isLeft(Y,X), format('~w is between ~w and ~w', [X,Y,Z]).


