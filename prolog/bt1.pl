owns_a_dog(john).
lover_of_animals(X):- owns_a_dog(X).
do_not_kill_animals(X):- lover_of_animals(X).
