import asyncio

from websockets import ConnectionClosedOK
from websockets.asyncio.server import serve


async def echo(websocket):
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