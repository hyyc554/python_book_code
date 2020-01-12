import asyncio


class Event_ts(asyncio.Event):
    # TODO: clear() method
    def set(self):
        # FIXME: The _loop attribute is not documented as public api!
        self._loop.call_soon_threadsafe(super().set)


def threaded(event):
    import time
    while True:
        event.set()
        time.sleep(1)


async def main():
    import threading
    e = Event_ts()
    threading.Thread(target=threaded, args=(e,)).start()
    while True:
        await e.wait()
        e.clear()
        print('whatever')


asyncio.ensure_future(main())
asyncio.get_event_loop().run_forever()
