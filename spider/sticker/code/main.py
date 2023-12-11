import re
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
url="https://www.biqugeg.cc/8_8465/26860982.html"
html = requests.get(url,headers=headers).text
#encode编码，将ISO-8859-1编码成unicode
html=html.encode("GBK")
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
print(section_text)

# py spider\sticker\data