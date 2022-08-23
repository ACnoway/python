# 后端：https://quanxiaoshuo.com/
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from global_var import get_value

head = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}  # 把浏览器的User-Agent贴进来，这里head也是一个字典


class search_UI(QtWidgets.QWidget):

    def show_UI(self):
        self.show()

    def setup_UI(self):
        self.resize(500, 700)
        self.setWindowTitle("搜索结果")
        self.mainshow = QtWidgets.QLabel(self)
        self.mainshow.resize(460, 660)
        # self.mainshow.move(20, 20)
        self.mainshow.setOpenExternalLinks(True)
        self.seearea = QtWidgets.QScrollArea(self)
        self.seearea.resize(500, 700)
        self.seearea.move(0, 0)
        self.seearea.setContentsMargins(50, 50, 50, 50)
        self.seearea.setWidget(self.mainshow)
        self.show_result()

    def show_result(self):
        name = get_value("name")
        a = "https://quanxiaoshuo.com/s_" + name
        print(a)
        jieguo = requests.get(url=a, headers=head, verify=False)
        jgsoup = BeautifulSoup(jieguo.text, "html.parser")
        jgcon = jgsoup.select(".main.list .list_content")
        jgall = ""
        for x in jgcon:
            jgall += str(x)
        self.mainshow.setText(jgall)

    def exec_(self):
        QtWidgets.QApplication.exec_()

    # def get(self,url):
