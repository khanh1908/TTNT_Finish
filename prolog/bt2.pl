isdog(fred, collie).
owns(fred, sam).
saturday(today).
cold(saturday).
trained(fred).
good_dog(spaniel).
good_dog:- trained(collie).
with(X, Y):- owns(X, Y), good_dog(X) .
at(sam, park):- saturday(today),\+ cold(saturday).
at(sam, museum):- saturday(today), cold(saturday).
loc(fred, X):- at(sam, X).
