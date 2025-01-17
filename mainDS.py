from collections import deque
'''
list = []
list.append('3')
list.append('5')
list.append('4')
list.append('3')
#list.remove(5)
list.pop(0)
#list.clear()
#print(list)
print(list.index('3'))
print(list.count('3'))
list.sort()
print(list)
list.reverse()
print(list)
'''
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

matrix = [
    [1, 2, 3],
    [4, 5 ,6],
]
print(matrix)


Mli = list(zip(*matrix))
print(Mli)

print(Mli.pop(0))

del Mli[1]

print(Mli)

tuple1 = ()

tuple2 = "rise",

tuple3 = 1 , '3' , "rom"

t = 12345, 54321, 'hello!'
x , y, z = t

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple3[0:2])
print(y)

basket = {'a','b','c','a','d'}
print(basket)

a= set('abcabdfg')
print(a)