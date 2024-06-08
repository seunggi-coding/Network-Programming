import asyncio

port = 2500
BUFSIZE = 1024

async def main():
    reader, writer = await asyncio.open_connection('localhost', port)
    while True:
        message = input('Enter message: ')
        if message == 'quit':
            break
        writer.write(message.encode())
        await writer.drain()
        
        data = await reader.read(BUFSIZE)
        print(f'Received: {data.decode()}')
    writer.close()
    
asyncio.run(main())