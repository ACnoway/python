# http://www.xiaoshuopu.com/
import re
import requests
from bs4 import BeautifulSoup
# from tqdm import trange
import time
# 头部伪装
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


def get_download(url, novel):
    while True:
        print("爬取内容中……")
        try:
            html = requests.get(url, headers=headers).text
            break
        except:
            print("爬取失败\n")
            time.sleep(1)
            print("重新爬取\n")
            continue
    # encode编码，将ISO-8859-1编码成unicode
    html = html.encode("utf-8")
    data = BeautifulSoup(html, "html.parser")
    # 获取每一章的章节名
    section_name = data.select(
        '#content #a_main #amain.bdsub dl dd')[0].text
    print(section_name)
    # 获取每一章节的文章内容
    section_text = data.select(
        '#content #a_main #amain.bdsub #htmlContent p')[0].text
    # print(section_text)
    # 规范内容格式
    # re.sub( '\s+', '\r\n\t', section_text)指的是将内容中含有多个空格的地方替换为 回车（空行）+ tab缩进
    # .strip('\r\n')指的是将内容开头和结尾的空行
    section_text = section_text.replace("   ", "\r\n")
    f = open(novel, 'a', encoding='utf-8')
    f.write(section_name + '\n\n')
    f.close()
    with open(novel, 'a', encoding='utf-8') as f:
        f.write(section_text + "\n")
    nexturl = data.select('#footlink a')[2]['href']
    okk = data.select('#footlink a')[2].text
    # print(okk)
    return nexturl, okk


if __name__ == '__main__':
    url = "http://www.xiaoshuopu.com/xiaoshuo/12/12910/29454494.html"
    novel = '陆地键仙.txt'
    rec = 
    i = 1
    while True:
        print("开始爬取第" + str(i) + "章")
        while True:
            try:
                next, ok = get_download(url, novel)
                break
            except:
                print("爬取失败\n")
                time.sleep(1)
                print("重新爬取\n")
                continue

        print("第" + str(i) + "章爬取完毕")
        i += 1
        url = "http://www.xiaoshuopu.com" + next
        if (ok == "书末章"):
            print("全本爬取完毕")
            break
