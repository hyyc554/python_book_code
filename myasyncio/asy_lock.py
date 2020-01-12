import asyncio
import random
import time
import concurrent.futures

queue_dict = {i: {"queue": asyncio.Queue()} for i in range(10)}


async def producer(queue_dict: dict):
    count = 0
    while True:
        label_id = random.randrange(10)
        # label_id = 1
        print(f"向{label_id}队列中放入：{count}")
        await queue_dict[label_id]["queue"].put(count)
        await asyncio.sleep(1)
        count += 1


def worker(label, msg):
    """
    这个函数来模拟一个必须由多线程来处理的阻塞操作
    :param label:
    :param msg:
    :return:
    """
    # 模拟一个IO操作
    time.sleep(2)
    # 处理完本次IO再来重置信号
    print(f"{label}的{msg}处理完毕")
    return 2333


async def consumer(label_id, loop, executor):
    while True:
        # print(f"{label_id}开始等待消息")
        msg = await queue_dict.get(label_id).get("queue").get()
        # print(f"{label_id}队列发来的{msg}")

        result = await loop.run_in_executor(executor, worker, label_id, msg)
        # print('custom thread pool', result)


async def main(loop):
    # 创建一个线程池，用来处理那些无法协程异步的操作（历史原因，python的大多数三方包都不支持协程异步）
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=300,
    )
    # 这里模拟一个生产者，定时的向内存队列内写入消息

    p_task = asyncio.create_task(producer(queue_dict))
    c_tasks = [asyncio.create_task(consumer(i, loop, executor))
               for i in range(10)]
    await asyncio.wait([p_task, *c_tasks])


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()
