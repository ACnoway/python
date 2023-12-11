import re
import requests
from bs4 import BeautifulSoup
#from tqdm import trange
import time
#头部伪装
headers = {
    'User-Agent':'Chrome/63.0.3239.132'
}
 
def get_download(url,novel):
    while True:
        try:
            print("爬取内容中……")
            html = requests.get(url,headers=headers).text
            break
        except:
            print("爬取失败\n")
            time.sleep(5)
            print("重新爬取\n")
            continue
    #encode编码，将ISO-8859-1编码成unicode
    #html=html.encode("GBK")
    data = BeautifulSoup(html,"html.parser")
    print(data)
    #获取每一章的章节名
    #获取每一章节的文章内容
    section_text = data.text
    #规范内容格式
    with open(novel,'a',encoding='utf-8') as f:
        f.write(section_text+"\n")
if __name__ == '__main__':
    url = "https://api.vvhan.com/api/love"
    novel = '文案.txt'
    num = 100 #共228章
    print
    for i in range(1000-628):
        print("开始爬取第"+str(i+1+628)+"条")
        get_download(url,novel)
        print("第"+str(i+629)+"章爬取完毕")
        time.sleep(1)