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
 
% timesOP multiplies first param for x number of times where x is second param and puts the result in the third param
timesOP(_,0,0).
timesOP(0,_,0).
timesOP(X,s(Y),Z) :- timesOP(X,Y,W),plus1(X, W, Z).   

%   powerOP
powerOP(0,_,0).
powerOP(_,0,s(0)).
powerOP(X,s(Y),Z) :- powerOP(X,Y,W), timesOP(X,W,Z).

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


%prependOP/3 insert to the FIRST position the elem @1 to the list@2 and return the resultant list @3

prependOP(X,List , [X|List]).

%appendOP/3 insert to the LAST position
appendOP(E,[],[E]).
appendOP(E,[H|T],R):- appendOP(E,T,K), prependOP(H,K,R).

%%appendListOP/3 insert all the elems of the first list @1 to the end of the second list @2 preserving original order of both
appendListOP( L , [], L).
appendListOP( L, [H|T] , K):- appendListOP( L , T , Y), prependOP( H, Y, K). 

%%insertInHeadOP/3 it inserts elems of @1 in head of the list @2
insertInHeadOP([],X,X).
insertInHeadOP([X|Rest],Y,Result) :- prependOP(X , W, Result) , insertInHeadOP(Rest,Y,W) .


%containedOP/2 checks that the elem which is the first param is contained in the set which is the second param
containedOP(X,[X|_]).
containedOP(X,[Y|List]) :- X\= Y, containedOP(X,List).

%notContainedOP/2 it checks if the element @1 is not contained in the set @2
notContainedOP(_, []).
notContainedOP(X, [H|T]):- X\=H, notContainedOP(X,T).


%%removeheadOP/2 remove the head of a list passed as first param; result is the second param
removeheadOP([_|Rest], Rest).

%%removeOP/3 remove the first occurence of the elem which is the first param from the list which is second param if it occurs and the result is third param
removeOP(_,[],[]).
removeOP(X,[X|Rest], Rest).
removeOP(X,[Y|Rest], Result) :- X\= Y,containedOP(X,Rest), removeOP(X,Rest,W), prependOP(Y,W,Result).

%%removeallOP/3 remove all the occurences of elem @1 in set @2 and return the resultant set @3
removeallOP(_,[],[]).
removeallOP(X,[X|Rest], Result):- removeallOP(X,Rest,Result).
removeallOP(X,[Y|Rest], Result) :- X\= Y, removeallOP(X,Rest,W), prependOP(Y,W,Result).

%%concatOP/3 it return the concatenation @3 between two sets @1 and @2
concatOP([],X,X).
concatOP([X|Rest],Y,Result) :- concatOP(Rest,Y,W), prependOP(X,W,Result).

%%concatAlternOP insert the elems of @1 at the beginning of @2 and return the resulting list in @3 
concatAlternOP( [] , X , X ).
concatAlternOP( [H| Tail] , L , [H| K] ) :- concatAlternOP( Tail , L , K).

%%intersectOP/3 returns the intersection of sets in first and second param as the third param
intersectOP([],_,[]).
intersectOP( [H|T],L,R):- containedOP(H,L), removeallOP(H,T,Tc), removeallOP(H,L,Lc), intersectOP(Lc,Tc,W),prependOP(H,W,R).
intersectOP([H|T],L,R):- removeallOP(H,T,Tc), intersectOP(L,Tc,R).

%%putoutOP/3 it returns a set @3 in which are all the elements of set @1 that don't occur in set @2  '
putoutOP([],_,[]).
putoutOP([H|T],Y,R):- containedOP(H,Y), putoutOP(T,Y,R).
putoutOP([H|T],Y,R):- notContainedOP(H,Y), putoutOP(T,Y,Partial), prependOP(H,Partial,R).

%%reverseOP/2
reverseOP([],[]).
reverseOP([H|T],Z):- reverseOP(T,K), appendOP(H,K,Z).

%%prefixOP/2 returns each atom @1 which is a valid prefix of the List @2
prefixOP([], _).
prefixOP( [H | Rest1], [H | Rest2]) :- prefixOP( Rest1, Rest2).

%%suffixOP/2 returns each atom @1 which is a suffix for the List @2 (inverse logic of prefixOP/2)
suffixOP( Suf, L):- reverseOP( L , R ), prefixOP( K, R) ,reverseOP( K, Suf).



%%sublistOP/2 returns each subset @1 made of contiguous elems that belong to the List @2 ( e.g. @2 [1,2,3]   @1 [];[1];[2];[3];[1,2];[2,3];[1,2,3] )
sublistOP([] , _).
sublistOP( X , List ):- prefixOP( X,  List).	
sublistOP( X , [_|Tail]):- sublistOP( X, Tail).


%unionOP/3 it will return the union of two sets @1 , @2  N.B. duplicates are mantained
unionOP( [], S , S).
unionOP( [H|Tail] , Set2 , Result) :-  containedOP( H, Set2), unionOP( Tail, Set2, Result).
unionOP( [H|Tail] , Set2 , Result) :-   unionOP( Tail, Set2, K ), concatOP( [H], K, Result).



%%subsetOP/2 checks that the first param @1 is contained in (is a subset of) the second param @2, ERROR infinite loop in the first element with this call? trace, subsetOP(O,[r,g,b,f]).
%% it works if @1 is not undefined (e.g. is a set [1,2] or [8,4,3]) but with an undefined input it will return wrong results (same results as a prefixOP execution) 
subsetOP([], _).
subsetOP( [X | Tail] , Set):-  containedOP( X , Set), removeOP(X, Set, New), subsetOP( Tail, New).


%insertionSortOP  it return an ordered list @2 computing an insertion sort policy given a list as param @1
%[1,3,2] -> []
%[3,2] -> [1]
%[2] -> [1,3]
%[] -> [1,2,3]

%insertionSortOP/2 main fun that given an unordered list of ints @1 return an ordered one @2
insertionSortOP([H|[]], [H]).
insertionSortOP([H|T], L):- insertionSortOP( T, K), orderedInsertionOP( H , K , L).

%%orderedInsertionOP/3 auxiliary fun: given an ordered list @2 insert the elem @1 avoiding multiple insertion following an increasing magnitude order returning the list @3
orderedInsertionOP( [] , L, L).
orderedInsertionOP( E , [] , [E] ).
orderedInsertionOP( E , [H|T] , L):- H > E, orderedInsertionOP( [] , T, K), prependOP( H, K, Y), prependOP( E, Y, L), !.
orderedInsertionOP( E , [H|T] , L):- H =< E, orderedInsertionOP( E , T, K), prependOP( H, K, L), !.



%%lenOP/2
lenOP( [] , 0).
lenOP( [_|T] , K):- lenOP( T, Y), K is Y+1. 

%%splitOneEachOP/3
splitOneEachOP( [], [], []):- !.
splitOneEachOP( [F|[S|T]], [F|B], [S|C] ):- splitOneEachOP( T, B ,C).



%%INTEGER BASED ARITHMETIC

%%sumOP/3
sumOP(A, B, C):- C is A+B.

%%multOP/3
multOP(A, B, C):- C is A*B.

%%greaterOP/2
greaterOP( G, L) :- G>L.

%%lesserOP/2
lesserOP( L ,G) :- L<G.

factoriel(0,1):- true, !.
factoriel(X,Y) :- X1 is X - 1, factoriel(X1,Z), Y is Z*X,!.


% GRAPHS OPERATIONS {VISIT, PATH, EXISTENCE}
arc(a,b).
arc(a,e).
arc(b,a).
arc(b,c).
arc(c,c).
arc(c,d).
arc(d,c).
arc(d,b).
arc(e,c).

pathOP(S,G,P):- pathOP(S,G,P,[S]).

pathOP( N, N, [N], _).
pathOP( S, G, [S|P], V):- arc( S, K), S\=K,  notContainedOP(K, V), pathOP(K, G, P , [K|V]).


childOP(X,Y):- arc(Y,X).
childrenOP(Father,List):- findall(Son,childOP(Son,Father),List).


%TREES AND LISTS OF LISTS

%tree(1,  tree(2, void,   tree( 3, void ,void)   ),  void)
%tree(1,  tree(2, void,   tree( 3, void ,void)   ),  tree(4, void,void) )

binary_tree(void).
binary_tree(tree(_Element,Left,Right)) :- binary_tree(Left), binary_tree(Right).


isotree(void,void).
isotree(tree(X,Left1,Right1),tree(X,Left2,Right2)) :- isotree(Left1,Left2), isotree(Right1,Right2).
isotree(tree(X,Left1,Right1),tree(X,Left2,Right2)) :- isotree(Left1,Right2), isotree(Right1,Left2).

preorder(void, [void]).
preorder(tree(X, Left, Right), CompleteList):- preorder(Left, LeftList), preorder(Right, RightList), concatOP([X|LeftList], RightList, CompleteList).

bf([], []).
bf([void | Rest], Ls):- bf(Rest, Ls).
bf([tree(I, Dx, Sx)| Rest], [I|Ls]):-	concatOP(Rest, [Sx, Dx], Nodes), bf(Nodes, Ls).



%%1. Write a PROLOG program counting the elements of a list of lists.
%%lenListOfListsOP/2
lenListOfListsOP( [] , 0).
lenListOfListsOP( [H|T] , K):- lenListOfListsOP( T , Y), lenOP(H, X), K is X+Y.



%%2. Write a PROLOG program which implements member for a binary tree.
%%memberBinTreeOP/2
memberBinTreeOP( tree( E , _ , _ ) , E ).
memberBinTreeOP( tree( _E, L, _R) , E):- memberBinTreeOP( L , E).
memberBinTreeOP( tree( _E, _L, R) , E):- memberBinTreeOP( R , E).




%%3. Write a PROLOG program which returns a list containing all the nodes at a given depth D of a binary tree.
%%nodesAtLevelOP/3  call >> nodesAtLevelOP( tree(1,  tree(2, void, void) , tree( 3, void ,void) ), 1, L).

nodesAtLevelOP( Tree, Depth , L) :- bagof( N, nodesAtLevelAuxOP( Tree, Depth, N), L).

nodesAtLevelAuxOP( tree( X, _L, _R) , 0 , X).
nodesAtLevelAuxOP( tree(_X, L, _R), D, X ):- K is D-1, nodesAtLevelAuxOP( L, K, X).
nodesAtLevelAuxOP( tree(_X, _L, R), D, X ):- K is D-1, nodesAtLevelAuxOP( R, K, X).


%%%4.  Consider the PROLOG terms representing the binary trees whose nodes are labelled
%%%   by a constant symbol and, in addition, store the depth of the node. Write a
%%%  PROLOG program that returns true if its argument is a binary tree as above specified.
%%atomDepthBinTreeOP/1  %% tree( [root, 0] , tree( [firstLeft, 1] , void , void ) , void ) 

atomDepthBinTreeOP( T ):- atomDepthBinTreeOP(T , 0 ).

%%atomDepthBinTreeOP/2
atomDepthBinTreeOP( void, _D).
atomDepthBinTreeOP( tree([X , D]  , void, void) , D):- atom(X).
atomDepthBinTreeOP( tree([X , D],L,R),D):-Y is D+1,atom(X),atomDepthBinTreeOP(L,Y),atomDepthBinTreeOP(R,Y).

%%%5. Write a PROLOG program that, given in input a binary tree and a constant,
%%% returns the depth of a node containing the given constant.
%%%depthInfoConstNodeDepthOP/3 call >>>depthInfoConstNodeDepthOP( tree( [root, 0] , tree( [firstLeft, 1] , tree( [ secondleft, 2],void,void ) , void ) , void ) ,root , L ).

depthInfoConstNodeDepthOP( tree( [Const,Depth] , _L, _R), Const, Depth):- atom(Const).
depthInfoConstNodeDepthOP( tree( [_X, _K],L, _R),C,Depth):- depthInfoConstNodeDepthOP(L,C,Depth).
depthInfoConstNodeDepthOP( tree( [_X, _K],_L, R),C,Depth):- depthInfoConstNodeDepthOP(R,C,Depth).


%%%6. Write a PROLOG program that, given in input a binary tree without the depth information
%%% on the nodes and a constant, returns the depth of a node containing the given constant.
%%constNodeDepthOP/3 >>>call constNodeDepthOP( tree( root, tree( firstleft, void,void) , tree(firstright, void, tree( secondrright, void, void))), secondrright, H ).

constNodeDepthOP( Tree, Const , Depth) :- atom(Const), constNodeDepthOP( Tree, Const , 0, Depth).

%%constNodeDepthOP/4
constNodeDepthOP( tree( Const , _L , _R ),Const,D,D).
constNodeDepthOP( tree( _X, L, _R),Const,D,U):- Y is D+1,constNodeDepthOP(L,Const,Y,U).
constNodeDepthOP( tree( _X, _L, R),Const,D,U):- Y is D+1,constNodeDepthOP(R,Const,Y,U).



%%%7.Write a PROLOG program that, given in input a binary tree without the depth information on
%%% the nodes, returns an isomorphic binary tree with the depth information stored in the nodes.
%%depthInfoInsertionOP/2
depthInfoInsertionOP( Tree, Result ):- depthInfoInsertionOP( Tree, 0 , Result).
%%depthInfoInsertionOP/3

depthInfoInsertionOP( void, _D , void ).
depthInfoInsertionOP(tree( X,L,R),D, tree( [X, D], W, Z)):- K is D+1,depthInfoInsertionOP(L,K,W),depthInfoInsertionOP(R,K,Z).

%%% isomorphicDepthInfoTreeOP/2    call>> isomorphicDepthInfoTreeOP( tree( 99 , tree(33, void, void) , void) ,L).
isomorphicDepthInfoTreeOP(Tree, Isotree):- depthInfoInsertionOP( Tree, Newtree), isotree(Newtree,Isotree).





%%8.Define the predicate notMember(X,L), true if X does not occur in the list L.
%%Provide a definition using NAF and one without it, and compare them.
% see notContainedOP/2  for the implementation without NAF

notMemberOP( E , L ):- not( containedOP( E, L)).


%%9.Define a predicate sortm(X,Y,Z), to order lists X and Y and return the result in Z, through merge-sort.
%%sortmOP/3

%%sublistsSeparatedAtLenOP/4
sublistsSeparatedAtLenOP( L, 0, [], L):-!.
sublistsSeparatedAtLenOP( [H|T], K , [H|U], G):- Y is K-1, sublistsSeparatedAtLenOP( T, Y, U, G). 


splitHalfOP( X, A,B):- lenOP( X, K), T is K//2, sublistsSeparatedAtLenOP(X, T, A,B).

concatsortedOP( [] , Y , Z):- insertionSortOP( Y, Z),!.
concatsortedOP( X, [], Z):- insertionSortOP( X, Z),!.
concatsortedOP( X, Y, Z):- concatOP( X,Y, W), insertionSortOP( W, Z).

sortmOP( [] , []):-!.
sortmOP( [X] , [X]):- !.
sortmOP( X , K) :- splitHalfOP( X , L, R) , sortmOP( L, W), sortmOP(R,Z), concatsortedOP( W, Z, K),!.












%>>checked until there.










%findall    :   bagof   : setof






%depthVisitRecOP/2 and depthVisitSuccOP/2 visit a possibly ciclic graph with a depth first policy
depthVisitSuccOP([],_).
depthVisitSuccOP([H|T], Rev):- depthVisitRecOP(H,Rev), depthVisitSuccOP(T,Rev).
%start from invocation of depthVisitRecOP with @2 param = [].
depthVisitRecOP(X,_):- childrenOP(X,[]).
depthVisitRecOP(X, Visited):- prependOP(X,Visited,Revisited), childrenOP(X,Successors), putoutOP(Successors,Visited,Ksucc), depthVisitSuccOP(Ksucc,Revisited).


%DFS with print of nodes visited.
dfsExpandedSuccOP([],_,_).
dfsExpandedSuccOP([H|T], Rev,Expanded):- dfsExpandedRecOP(H,Rev,Expanded), dfsExpandedSuccOP(T,Rev,Expanded).

dfsExpandedRecOP(X,_,_):- childrenOP(X,[]).
dfsExpandedRecOP(X, Visited,Result):- prependOP(X,Visited,Revisited), prependOP(X,Expanded,Result), childrenOP(X,Successors), putoutOP(Successors,Visited,Ksucc), dfsExpandedSuccOP(Ksucc,Revisited,Expanded).






