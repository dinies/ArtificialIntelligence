% NUMBERS PROPERTIES
% express natural numbers in a recursive way through 's()' successor function
natural_number(0).
natural_number(s(X)) :- natural_number(X).

% plus1 checks that first param + second param is equal to third param
plus1(0,X,X) :- natural_number(X).
plus1(s(X),Y,s(Z)):- plus1(X,Y,Z).

% lesseq1 checks that first param is <= of second param
lesseq1(0,X) :- natural_number(X).
lesseq1(s(X),s(Y)) :- lesseq1(X,Y).
 
% timesOP multiplies first param of x number of times where x is second param and puts the result in the third param
timesOP(_,0,0).
timesOP(0,_,0).
timesOP(X,s(Y),Z) :- timesOP(X,Y,W),plus1(X, W, Z).   

%   powerOP
powerOP(0,_,0).
powerOP(_,0,s(0)).
powerOP(X,s(Y),Z) :- powerOP(X,Y,W), timesOP(W,X,Z).

% factorialOP computes the factorial of the first argument and return the result in the secon argument
factorialOP(0,s(0)).
factorialOP(s(X),Z) :- factorialOP(X,W), timesOP(s(X), W, Z). 

% minimumOP (elem, elem, result) return the element with the minimum value between first and second param
minimumOP(X,X,X).
minimumOP(0,_,0).
minimumOP(_,0,0).
minimumOP(X, Y, X):-  X\= Y, lesseq1(X, Y).
minimumOP(X,Y,Y):- X\= Y, lesseq1(Y,X).

% SET OPERATIONS {LISTS}


%appendOP/2 append the elem which is the first param to the list which is the second param and return the resultant list in the third param
appendOP(X,List , [X|List]).

addToTheBackOP(E,[],[E]).
addToTheBackOP(E,[H|T],R):- addToTheBackOP(E,T,K), appendOP(H,K,R).

%containedOP/2 checks that the elem which is the first param is contained in the set which is the second param
containedOP(X,[X|_]).
containedOP(X,[Y|List]) :- X\= Y, containedOP(X,List).

%notContainedOP/2 it checks if the element @1 is not contained in the set @2
notContainedOP(_, []).
notContainedOP(X, [H|T]):- X\=H, notContainedOP(X,T).

%%subsetOP/2 checks that the first param is contained in (is a subset of) the second param, ERROR infinite loop in the first element with this call? trace, subsetOP(O,[r,g,b,f]).
subsetOP([],_).
subsetOP([X|Rest], Set) :-  containedOP(X,Set), removeallOP(X,Set,K), subsetOP(Rest,K).

%%removeheadOP/2 remove the head of a list passed as first param; result is the second param
removeheadOP([_|Rest], Rest).

%%removeOP/3 remove the first occurence of the elem which is the first param from the list which is second param if it occurs and the result is third param
removeOP(_,[],[]).
removeOP(X,[X|Rest], Rest).
removeOP(X,[Y|Rest], Result) :- X\= Y,containedOP(X,Rest), removeOP(X,Rest,W), appendOP(Y,W,Result).

%%removeallOP/3 remove all the occurences of elem @1 in set @2 and return the resultant set @3
removeallOP(_,[],[]).
removeallOP(X,[X|Rest], Result):- removeallOP(X,Rest,Result).
removeallOP(X,[Y|Rest], Result) :- X\= Y, removeallOP(X,Rest,W), appendOP(Y,W,Result).

%%concatOP/3 it return the concatenation @3 between two sets @1 and @2
concatOP([],X,X).
concatOP([X|Rest],Y,Result) :- concatOP(Rest,Y,W), appendOP(X,W,Result).

%%intersectOP/3 returns the intersection of sets in first and second param as the third param
intersectOP([],_,[]).
intersectOP( [H|T],L,R):- containedOP(H,L), removeallOP(H,T,Tc), removeallOP(H,L,Lc), intersectOP(Lc,Tc,W),appendOP(H,W,R).
intersectOP([H|T],L,R):- removeallOP(H,T,Tc), intersectOP(L,Tc,R).

%%putoutOP/3 it returns a set @3 in which are all the elements of set @1 that don't occur in set @2  '
putoutOP([],_,[]).
putoutOP([H|T],Y,R):- containedOP(H,Y), putoutOP(T,Y,R).
putoutOP([H|T],Y,R):- notContainedOP(H,Y), putoutOP(T,Y,Partial), appendOP(H,Partial,R).

%%reverseOP
reverseOP([],[]).
reverseOP([H|T],Z):- reverseOP(T,K), addToTheBackOP(H,K,Z).

%%suffixOP if you ask him something with an indefinite variable it will loop undefinitely probably because reverseOP is not robust enought.
suffixOP(L,J):- reverseOP(L,X), reverseOP(J,Y),suffixRecOP(X,Y).
suffixRecOP([],_).
suffixRecOP([H|Tx],[H|Ty]):- suffixRecOP(Tx,Ty).



%>>checked until there.

%insertionSortOP  it return an ordered list computing an insertion sort policy
%[1,3,2] -> []
%[3,2] -> [1]
%[2] -> [1,3]
%[] -> [1,2,3]


insertionSortOP  

% GRAPHS AND TREES OPERATIONS {VISIT, PATH, EXISTENCE}
arc(a,b).
arc(a,c).
arc(c,a).
arc(c,e).

childOP(X,Y):- arc(Y,X).
childrenOP(Father,List):- findall(Son,childOP(Son,Father),List).


%depthVisitRecOP/2 and depthVisitSuccOP/2 visit a possibly ciclic graph with a depth first policy
depthVisitSuccOP([],_).
depthVisitSuccOP([H|T], Rev):- depthVisitRecOP(H,Rev), depthVisitSuccOP(T,Rev).
%start from invocation of depthVisitRecOP with @2 param = [].
depthVisitRecOP(X,_):- childrenOP(X,[]).
depthVisitRecOP(X, Visited):- appendOP(X,Visited,Revisited), childrenOP(X,Successors), putoutOP(Successors,Visited,Ksucc), depthVisitSuccOP(Ksucc,Revisited).


%DFS with print of nodes visited.
dfsExpandedSuccOP([],_,_).
dfsExpandedSuccOP([H|T], Rev,Expanded):- dfsExpandedRecOP(H,Rev,Expanded), dfsExpandedSuccOP(T,Rev,Expanded).

dfsExpandedRecOP(X,_,_):- childrenOP(X,[]).
dfsExpandedRecOP(X, Visited,Result):- appendOP(X,Visited,Revisited), appendOP(X,Expanded,Result), childrenOP(X,Successors), putoutOP(Successors,Visited,Ksucc), dfsExpandedSuccOP(Ksucc,Revisited,Expanded).


