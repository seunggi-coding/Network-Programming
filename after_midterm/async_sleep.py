import time, asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(
        say_after(1, 'hello')
    )
    task2 = asyncio.create_task(
        say_after(2, 'world')
    )
    
    await task1
    await task2
    
    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())