"""
Future
future是一个数据结构，表示还未完成的工作结果。
事件循环可以监视Future对象是否完成。
从而允许应用的一部分等待另一部分完成一些工作。
"""
import asyncio

def foo(future,result):
    print(f"此时future的状态:{future}")
    print(f"设置future的结果:{result}")
    future.set_result(result)
    # 调用set_result之后future对象的状态由pending变为finished
    print(f"此时future的状态:{future}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        loop.call_soon(foo, all_done, "Future is done!")
        print("进入事件循环")
        result = loop.run_until_complete(all_done)
        print("返回结果", result)
    finally:
        print("关闭事件循环")
        loop.close()
    print("获取future的结果", all_done.result())

"""
进入事件循环
此时future的状态:<Future pending cb=[_run_until_complete_cb() at c:\python36\Lib\asyncio\base_events.py:185]>
设置future的结果:Future is done!
此时future的状态:<Future finished result='Future is done!'>
返回结果 Future is done!
关闭事件循环
获取future的结果 Future is done!
"""

