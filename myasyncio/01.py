def regular_double(x):
    return 2 * x


async def async_double(x):
    return 2 * x


# <class 'function'> <class 'int'> 函数、执行结果是整数
print(type(regular_double), type(regular_double(1)))
# <class 'function'> <class 'coroutine'> 函数、执行结果是一个协程
print(type(async_double), type(async_double(1)))
