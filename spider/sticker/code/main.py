import re
import requests
from bs4 import BeautifulSoup
import json
import os

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


def down(url, save, name):
    html = requests.get(url, headers=headers, timeout=20).content
    f = open(f"{save}/{name}.png", "wb")
    f.write(html)


def main():
    print("这是一个适用于 store.line.me 的表情包爬取工具，请将详情链接复制下来并粘贴，会下载到当前目录的dist文件夹内")
    print("请选择爬取类型：\n1. Stickers\n2. Emoji")
    patype = int(input())
    url = input("请输入要爬取的表情包链接：")
    try:
        html = requests.get(url, headers=headers, timeout=20).text
    except:
        return
    if not os.path.exists("dist"):
        os.mkdir("dist")
    data = BeautifulSoup(html, "html.parser")
    if patype == 1:
        stickers = data.select(".mdCMN09Ul.FnStickerList li")
    else:
        stickers = data.select(".mdCMN09Ul.FnEmoji_animation_list_img li")
    for sticker in stickers:
        stimeta = json.loads(sticker.attrs["data-preview"])
        staticp = stimeta["staticUrl"]
        anip = stimeta["animationUrl"]
        if stimeta["type"] == "static":
            down(staticp, "dist", stimeta["id"])
        else:
            down(anip, "dist", stimeta["id"])


main()
input("按任意键退出")
