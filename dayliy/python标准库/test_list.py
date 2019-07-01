a = [ i % 2 for i in range(10) ]
b = ( i % 2 for i in range(10) )
print(type(a),a)
print(type(b),b)

# <class 'list'> [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# <class 'generator'> <generator object <genexpr> at 0x00000000028E62B0>