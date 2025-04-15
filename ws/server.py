import asyncio

from websockets import ConnectionClosedOK
from websockets.asyncio.server import serve


# websocket object docs https://websockets.readthedocs.io/en/stable/reference/asyncio/server.html#websockets.asyncio.server.ServerConnection
async def echo(websocket):
    # also message = await websocket.recv()
    async for message in websocket:
        try:
            await websocket.send(message)
        except ConnectionClosedOK:
            break


async def main():
    async with serve(echo, "0.0.0.0", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())