horse(tom).
horse(ken).
horse(kit).
horse(bin).
mother(tom, bin).
mother(tom, ken).
mother(bin, kit).
fast(kit).
fast(bin).
value(X):-mother(tom,X),fast(X).
