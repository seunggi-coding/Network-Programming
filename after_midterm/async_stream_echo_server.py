# client 프로그램은 echo_client.py 사용

import asyncio

port = 2500
BUFSIZE = 1024

async def handler_echo(reader, writer):
    while True:
        data = await reader.read(BUFSIZE)
        addr = writer.get_extra_info('peername')
        print(f'Received {data.decode()!r} from {addr}')
        
        writer.write(data)
        await writer.drain()
        print(f'Send: {data.decode()!r}')
        
async def main():
    server = await asyncio.start_server(
        handler_echo, '', port)
    
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    await server.serve_forever()
    
asyncio.run(main())