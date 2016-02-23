import asyncio

@asyncio.coroutine
def slow_operation(future):
    print('start slow_operation')
    yield from asyncio.sleep(1)
    print('set future done')
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.async(slow_operation(future))
future.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    loop.close()
