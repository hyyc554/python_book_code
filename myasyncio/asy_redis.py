import asyncio
import aioredis
import time

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task2

    print(f"finished at {time.strftime('%X')}")
task1 = asyncio.create_task(
    say_after(1, 'hello'))
asyncio.run(asyncio.wait( [task1 for i in range(1000) ]))
print("ok")
# asyncio.run(main())

# async def go():
#     redis = await aioredis.create_redis_pool(
#         'redis://192.168.0.119:6379/0',password="hyc554",maxsize=300)
#     # await redis.set('my-key', 'value')
#     print("start")
#     a = time.time()
#     for i in range(10):
#         await asyncio.sleep(1)
#         print(f"{i} work done!")
#         # val = await redis.get('106_sos', encoding='utf-8')
#     b = time.time()
#     print(b - a)
#     redis.close()
#     await redis.wait_closed()
#
#
# asyncio.run(main())