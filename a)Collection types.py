"""

Temario:

1.- Diccionarios
2.- In and not in
3.- Function get
4.- Tuples
5.- Tuple unpacking
6.- * Prefaced
7.- Sets
8.- Sets with magical operations
9.- Lists comprehensions
"""


#Diccionarios
ages = {
    "Mary":23,
    "David":25,
    "Samuel":28
}
print(ages["David"])

#In and not in
print("Samuel" in ages)
print(25 in ages)     #Dará false
print("Ivan" not in ages)

#Function get
print(ages.get("Mary"))
print(ages.get(12345, "not found"))
print(ages.get("David", "not found"))

#Tuples  (son inmutables, no pueden cambiar)
words = ("Hola", "Iván", "Adiós")
words1 = "Hola", "Andres", "Adiós"    #También se pueden crear sin paréntesis
print(words[1])
#words[1] = "Andres"    #Dará error tratar de cambiar su valor
print(words1[1])

#Tuple unpacking
numbers = (1,2,3)
a, b, c = numbers
print(a)
print(b)
print(c)
print(a+b)
a, b = b, a
print(a)
print(b)

#* prefaced
a, b, *c, d = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(a,b,c,d)
a, b, *c, d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a,b,c,d)

#sets
nums_set = {1,2,3,4,5,6,7,8}
print(3 in nums_set)           #lo mismo que listas o diccionarios pero se supone que es más rápido
print(nums_set)
nums_set.add(9)
nums_set.remove(3)
print(nums_set)

#sets with magical operations
nums = {1,2,3,4,5,6,7,8}
nums1 = {1,2,3,4,5,6}

print(nums | nums1) #combina dos sets en donde dejará los items de ambas listas sin repetirse
print(nums & nums1)  #dejará solamente los items que estén en ambos sets
print(nums - nums1)  #restará los items que haya en el segundo al primer set
print(nums1 - nums)
print(nums ^ nums1)  #items en cualquera pero no en ambos

#List comprehensions
cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i % 2 == 0]
print(evens)