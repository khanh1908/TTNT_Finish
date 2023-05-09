number(X,[X|_]).
number(X,[_|T]):-member(X,T).
