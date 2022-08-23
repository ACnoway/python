# 后端：https://quanxiaoshuo.com/
import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QApplication, QScrollArea, QFrame
from PyQt5.QtCore import QCoreApplication
from search import search_UI
from global_var import init, set_value
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

head = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}  # 把浏览器的User-Agent贴进来，这里head也是一个字典


class main_UI(QWidget):

    def show_UI(self):
        self.show()

    def setup_UI(self):
        init()
        self.setMinimumWidth(250)
        self.resize(250, 136)
        self.setWindowTitle("本地小说阅读器")
        self.layout = QVBoxLayout()
        # 预览四个边都预留20pixs的边界
        self.layout.setContentsMargins(20, 20, 20, 20)
        # 网格之间设置10pixs的间隔
        self.layout.setSpacing(10)

        self.search = QLineEdit(self)
        self.search.setPlaceholderText("请输入要搜索的书名，回车进行搜索")
        self.search.setMinimumHeight(30)
        self.search.textChanged.connect(self.searchin)
        self.search.returnPressed.connect(self.show_result)
        self.name = ""
        self.layout.addWidget(self.search, 0)

        self.history = QPushButton("阅读历史", self)
        self.layout.addWidget(self.history, 1)

        self.exitt = QPushButton("退出", self)
        self.exitt.clicked.connect(QCoreApplication.instance().quit)
        self.layout.addWidget(self.exitt, 2)
        self.setLayout(self.layout)

        self.tell = QLabel(self)
        self.tell.setOpenExternalLinks(True)
        self.layout.addWidget(self.tell, 3)
        self.check()

        self.mainshow = QLabel(self)
        self.mainshow.resize(460, 660)
        # self.mainshow.move(20, 20)
        self.mainshow.setOpenExternalLinks(True)
        self.mainshow.hide()

        self.seearea = QScrollArea(self)
        self.seearea.resize(300, 490)
        self.seearea.move(0, 0)
        self.seearea.setContentsMargins(50, 50, 50, 50)
        self.seearea.
        self.seearea.setWidget(self.mainshow)
        self.seearea.hide()

        self.layer = 0

    def check(self):
        a = requests.get(url="https://quanxiaoshuo.com/",
                         headers=head,
                         verify=False)
        if a.status_code // 100 == 2:
            self.tell.setText(
                "后端 by <a href=\"https://quanxiaoshuo.com/\">全小说</a>   连接成功！")
            set_value("sta", True)
        else:
            self.tell.setText(
                "后端 by <a href=\"https://quanxiaoshuo.com/\">全小说</a>   连接失败，请关闭本软件后重试"
            )
            set_value("sta", False)

    def searchin(self, s):
        self.name = s

    def show_result(self):
        a = "https://quanxiaoshuo.com/s_" + self.name
        print(a)
        jieguo = requests.get(url=a, headers=head, verify=False)
        jgsoup = BeautifulSoup(jieguo.text, "html.parser")
        jgcon = jgsoup.select(".main.list .list_content")
        jgall = ""
        for x in jgcon:
            jgall += str(x)
        self.mainshow.setText(jgall)
        self.mainshow.adjustSize()
        # self.search.hide()
        # self.history.hide()
        # self.exitt.hide()
        # self.tell.hide()
        self.mainshow.show()
        self.seearea.show()
        self.layer = 1
        self.resize(300, 500)

    def open(self):
        self.sui = search_UI()
        self.sui.setup_UI()
        self.sui.show_UI()
        self.sui.exec_()

    # def get(self,url):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = main_UI()
    a.setup_UI()
    a.show_UI()
    app.exec_()
