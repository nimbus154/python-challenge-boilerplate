import asyncio

# doc ref https://docs.python.org/3/library/asyncio-stream.html

async def handle_echo(reader, writer):
    addr = writer.get_extra_info("peername")
    async for data in reader:
        message = data.decode().rstrip()
        print(f"Received {message!r} from {addr!r}")
        print(f"Echoing: {message!r}")
        writer.write(data)
        await writer.drain()

    print(f"Closing connection to {addr}")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_echo, "0.0.0.0", 8888)
    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())