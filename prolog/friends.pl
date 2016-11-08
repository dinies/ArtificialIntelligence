friend(alessia, francesco).
friend(francesco,alessia).
friend(alex,alessia).
friend(alex,francesco).
friend(alex,rita).
friend(rita,alex).
friend(francesco,alex).
friend(francesco,giorgia).
friend(giorgia,francesco).
friend(alessia,alex).

friend(edoardo,francesco).
friend(edoardo,alex).
friend(francesco,edoardo).
friend(alex,edoardo).

male(edoardo).
male(alex).
male(francesco).
female(giorgia).
female(rita).
female(alessia).

country(edoardo,roma).
country(alex,sabaudia).
country(francesco,roma).
country(giorgia,milano).
country(rita,aprilia).
country(alessia,roma).


myFriends(Me,FriendList) :- findall(X, friend(X,Me), FriendList).


%PROBBLEM infinite loops with Ram crash.
%removeElement([],[]).
%removeElement([H|T], List) :- male(H), removeElement([T], ReturnList), List is [H|ReturnList].
%removeElement([_|T], List) :- removeElement([T], ReturnList),  List is ReturnList.
appendMale([],[]).
appendMale([H|T],List):- male(H), appendMale([T],L), List is [H|L].
appendMale([_|T],List):- appendMale([T],L), List is L.
 
%PROBLEM because there are too much arguments in findall due to the third arg added.

myFemaleFriends(Me,FriendList) :- female(X), findall(X, friend(X,Me), FriendList).
myMaleFriends(Me,Result) :- findall(X, friend(X,Me), FriendList), Param is [], removeElement(FriendList,Param), Result is Param.
myCityFriends(Me,FriendList) :- country(Me,Town), country(X,Town), findall(X,friend(X,Me), FriendList).

countList([],0).
countList([_|T],N) :- countList(T,N1), N is N1 + 1.

countMyFriends(Me,N) :- myFriends(Me, List), countList(List,M), N is M.
countMyFemaleFriends(Me,N) :- myFemaleFriends(Me, List), countList(List,M), N is M.
countMyMaleFriends(Me,N) :- myMaleFriends(Me, List), countList(List,M), N is M.
countMyTownFriends(Me,N) :- myCityFriends(Me,List), countList(List, M), N is M.


%countRecursive(Me,Node,1):- friend(Me,Node).


filterMale([],[]).
filterMale([H|T], List) :-  male(H), filterMale(T, L), List is [H|L].
filterMale([_|T], List) :- filterMale(T, L), List is L.
tryFilterMan(Me,N) :- myFriends(Me, List), filterMale( List, Return), countList(Return, M), N is M.
