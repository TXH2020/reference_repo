#!/usr/bin/env python

import asyncio
import websockets


async def echo(websocket):
    for i in ['hello','my','name','is','Tejas','Hegde']:
        await websocket.send(i)


async def main():
    async with websockets.serve(echo, "localhost", 8080):
        await asyncio.Future()  # run forever

asyncio.run(main())