import asyncio


async def num(n):
    try:
        await asyncio.sleep(n * 0.1)
        return n
    except asyncio.CancelledError:
        print(f"数字{n}被取消")
        raise


async def main():
    tasks = [num(i) for i in range(10)]
    complete = await asyncio.gather(*tasks)
    for i in complete:
        print("当前数字", i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
"""
当前数字 0
当前数字 1
当前数字 2
当前数字 3
当前数字 4
当前数字 5
当前数字 6
当前数字 7
当前数字 8
当前数字 9

"""