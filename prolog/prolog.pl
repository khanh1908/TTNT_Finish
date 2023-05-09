is_people(khanh).
is_animal(cat).
talk(X):-is_people(X).
sound(X):-is_animal(X).
