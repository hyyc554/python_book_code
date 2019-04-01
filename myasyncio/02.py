import asyncio


async def foo():
    print("这是一个协程")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("开始运行协程")
        coro = foo()
        print("进入事件循环")
        loop.run_until_complete(coro)
    finally:
        print("关闭事件循环")
        loop.close()
# 开始运行协程
# 进入事件循环
# 这是一个协程
# 关闭事件循环
