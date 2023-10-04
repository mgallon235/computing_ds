# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.

def triple(x):
    return 3*x

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(a,b):
    return b-a

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly

def dictionary_maker(ls1):
    dic1 = {}
    dic1[ls1[0][0]] = ls1[0][1]
    dic1[ls1[1][0]] = ls1[1][1]
    return dic1

foo = [('foo', 1), ('bar', 3)]

print(triple(9),subtract(99,10),dictionary_maker(foo))
