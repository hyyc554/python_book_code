import asyncio

async def foo():
    print("这是一个协程")
    return "返回值"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        print("开始运行协程")
        coro = foo()
        result = loop.run_until_complete(coro)
        print(f"run_until_complete可以获取协程的{result}，默认输出None")
    finally:
        print("关闭事件循环")
        loop.close()