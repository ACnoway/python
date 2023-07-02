import threading
import asyncio
import websockets


async def fasong(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        recv_text = await websocket.recv()
        print(recv_text)


async def jieshou(uri):
    while True:
        recv_text = await websockets.recv()
        print("> {}".format(recv_text))


message = input("请输入要发送的信息：")
uri = 'ws://192.168.3.20:8765'

asyncio.run(fasong(uri, message))