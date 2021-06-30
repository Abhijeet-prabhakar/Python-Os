from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showNormal()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction('⇤Back ', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        front_button = QAction('Forward⇥', self)
        front_button.triggered.connect(self.browser.forward)
        navbar.addAction(front_button)

        reload_button = QAction('⟳Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_butt = QAction('🏠Home page', self)
        home_butt.triggered.connect(self.navigate_home)
        navbar.addAction(home_butt)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Very Cool Browser')
window = MainWindow()
app.exec_()
