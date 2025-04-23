import asyncio

# doc ref https://docs.python.org/3/library/asyncio-stream.html
async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        "localhost", 8888)

    print(f"Send: {message!r}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Received: {data.decode()!r}")

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(tcp_echo_client("Hello World!\n"))