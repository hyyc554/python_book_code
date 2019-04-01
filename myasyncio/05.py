import asyncio
import functools


def callback(args,*,kwargs="defalut"):
    print(f"普通函数做为回调函数,获取参数:{args},{kwargs}")

async def main(loop):
    print("注册callback")
    loop.call_soon(callback,1)
    wrappend = functools.partial(callback,kwargs="not defalut")
    loop.call_soon(wrappend,2)
    await asyncio.sleep(0.2)

if __name__ == "__main__":
    loop= asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()


"""
注册callback
普通函数做为回调函数,获取参数:1,defalut
普通函数做为回调函数,获取参数:2,not defalut
"""
    