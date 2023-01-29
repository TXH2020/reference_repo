#!/usr/bin/env python

import asyncio
import websockets
from flask import *
app=Flask(__name__)
@app.route('/',methods=['POST'])
def get():
 async def hello():
    async with websockets.connect("ws://localhost:8080") as websocket:
        await websocket.send(json.dumps(request.values))
        for i in await websocket.recv():
            print(i)
 asyncio.run(hello())
 return make_response("sent")