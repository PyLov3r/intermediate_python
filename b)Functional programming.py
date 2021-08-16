"""

Temario:
1.- Higher order functions
2.- Lambdas
3.- Map
4.- Filter
5.- Generators
6.- Decorators
7.- Recursion
8.- Arg y kwargs

"""

#Higher order functiones
def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five,10))

#Lambdas
def my_func(f, arg):
    return f(arg)

my_func(lambda x: x + 5, 5)

print((lambda y: y + 5)(5))

#Map
def add_five(x):
    return x + 5

nums = [11,22,33,44,55]
result = list(map(add_five, nums))
print(result)

nums2 = [11,22,33,44,55]
result2 = list(map(lambda x: x+5, nums))
print(result2)

nums1 = [i + 5 for i in nums]
print(nums1)

#Filter
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

#Generators
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(20)))

#Decorators
def decor(func):
    def wrap():
        print("==============")
        func()
        print("===============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text()

#Recursion
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(20))
print(is_even(23))

#Args y Kwargs
def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1,2,3,4,5,6)



def my_func23(x, y=7, *args, **kwargs):
    print(args)
    print(kwargs)
    print(y)

my_func23(2,3,4,5,6, a=7, b=8)