"""
把函数视作对象
"""


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
print(help(factorial))

"""
- 
"""

fact = factorial
print(fact)
fact(5)
a = [i for i in map(fact,range(11))]

print(a)