my_dict = {'Roman' : 1954, 'Ivan' : 1985, 'Nina' : 2005}
print(my_dict)
print(my_dict['Roman'])
print(my_dict.get('Vova'))
my_dict.update({'Vova' : 2008, 'Kris' : 1966})
print(my_dict)
del my_dict['Roman']
print(my_dict.get('Roman', 1954))
print(my_dict)

my_set = {5, 7, 200, 'Air', True, 22, 22, 7, 'Air'}
print(my_set)
my_set = {5, 7, 200, 'Air', True, 22, 22, 7, 'Air', (2552221, 'LOLOLOLO')}
print(my_set)
print(my_set.discard(22))
print(my_set)