import asyncio
import websockets
import time
import threading


class CListen(threading.Thread):

    def __init__(self, loop):
        threading.Thread.__init__(self)
        self.mLoop = loop

    def run(self):
        asyncio.set_event_loop(self.mLoop)  # 在新线程中开启一个事件循环
        self.mLoop.run_forever()


async def echo(websocket, path):
    async for message in websocket:
        print(message)
        message = "I got your message: {}".format(message)
        await websocket.send(message)

        while True:
            t = input("输入")
            await websocket.send(t)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()