import websockets
import threading
import asyncio
import datetime

gLock = threading.Lock()


class CListen(threading.Thread):

    def __init__(self, loop):
        threading.Thread.__init__(self)
        self.mLoop = loop

    def run(self):
        asyncio.set_event_loop(self.mLoop)  # 在新线程中开启一个事件循环
        self.mLoop.run_forever()


async def fasong(websocket, message):
    await websocket.send(message)
    recv_text = await websocket.recv()
    print(recv_text)


async def jieshou(websocket):
    print("recieving\n")
    while True:
        recv_text = await websocket.recv()
        print("> {}".format(recv_text))


async def clientRun():
    async with websockets.connect("ws://192.168.3.20:8765") as websocket:
        asyncio.run_coroutine_threadsafe(fasong(websocket, message), newLoop)
        asyncio.run_coroutine_threadsafe(jieshou(websocket), newLoop)


if __name__ == '__main__':
    # websockets.serve()

    global message
    message = input("请输入要发送的信息：")
    
    global newLoop
    newLoop = asyncio.new_event_loop()
    listen = CListen(newLoop)
    # listen.setDaemon(True)
    listen.start()
