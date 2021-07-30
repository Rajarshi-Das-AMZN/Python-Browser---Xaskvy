# Rajarshi Das, 30-07-2021

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back
        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward
        fwd_btn = QAction('->', self)
        fwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fwd_btn)

        # refresh
        rfs_btn = QAction('(-)', self)
        rfs_btn.triggered.connect(self.browser.reload)
        navbar.addAction(rfs_btn)

        # home button
        home = QAction('Home', self)
        home.triggered.connect(self.navigate_home)
        navbar.addAction(home)

        # url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Xavsky')
window = MainWindow()
app.exec_()