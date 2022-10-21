# How would you confirm that 2 strings have the same identity?
animals           = ['python','gopher']
more_animals      = animals
print(animals == more_animals) #=> True
print(animals is more_animals) #=> True
even_more_animals = ['python','gopher']
print(animals == even_more_animals) #=> True
print(animals is even_more_animals) #=> False