import re
import requests
from bs4 import BeautifulSoup
#from tqdm import trange
import time
#头部伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
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
    #获取每一章的章节名
    section_name = data.title.string
    print(section_name)
    #获取每一章节的文章内容
    section_text = data.select('#wrapper .book.reader .content #content.showtxt')[0].text        
    #规范内容格式
    #re.sub( '\s+', '\r\n\t', section_text)指的是将内容中含有多个空格的地方替换为 回车（空行）+ tab缩进
    #.strip('\r\n')指的是将内容开头和结尾的空行
    section_text=re.sub( '\s+', '\r\n\t', section_text).strip('\r\n')
    f=open(novel,'a',encoding='utf-8')
    f.write(section_name+'\n')
    f.close()
    with open(novel,'a',encoding='utf-8') as f:
        f.write(section_text+"\n")
    pt_nexturl = 'var next_page = "(.*?)"'
    nexturl_num = re.compile(pt_nexturl).findall(str(data))
    nexturl = nexturl_num[0]
    return nexturl
if __name__ == '__main__':
    url = "https://www.biqugeg.cc/8_8465/26860982.html"
    novel = '都市超强神医.txt'
    num = 2500 #共228章
    for i in range(num):
        print("开始爬取第"+str(i+1)+"章")
        next=get_download(url,novel)
        
        print("第"+str(i+1)+"章爬取完毕")
        url = "https://www.biqugeg.cc"+next
        if(url == 'https://www.biqugeg.cc/8_8465/'):
            print("全本爬取完毕")
            break
