import asyncio


async def num(n):
    try:
        await asyncio.sleep(n*0.1)
        return n
    except asyncio.CancelledError:
        print(f"数字{n}被取消")
        raise


async def main():
    tasks = [num(i) for i in range(10)]
    complete, pending = await asyncio.wait(tasks, timeout=0.5)
    for i in complete:
        print("当前数字",i.result())
    if pending:
        print("取消未完成的任务")
        for p in pending:
            p.cancel()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

"""
当前数字 3
当前数字 1
当前数字 2
当前数字 4
当前数字 0
取消未完成的任务
数字5被取消
数字7被取消
数字9被取消
数字8被取消
数字6被取消
"""

"""
结果并没有按照数字的顺序显示
在内部wait()使用一个set保存它创建的Task实例
因为set是无序的所以这也就是我们的任务不是顺序执行的原因
wait的返回值是一个元组，包括两个集合，分别表示已完成和未完成的任务
"""