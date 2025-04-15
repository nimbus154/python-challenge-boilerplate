import asyncio
import sys

from websockets.asyncio.client import connect


async def hello():
    # websocket object client docs https://websockets.readthedocs.io/en/stable/reference/asyncio/client.html#websockets.asyncio.client.ClientConnection
    async with connect("ws://localhost:8765") as websocket:
        while True:
            message = sys.stdin.readline()
            if message == "exit":
                break
            await websocket.send(message)
            echo = await websocket.recv()
            print(echo)


if __name__ == "__main__":
    asyncio.run(hello())