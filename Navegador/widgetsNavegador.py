#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       simpleweb.py
#
#       Copyright 2013 Recursos Python - www.recursospython.com
#
#
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QMetaObject, QUrl
from PyQt4.QtGui import QHBoxLayout, QMainWindow, QWidget
from PyQt4.QtWebKit import QWebView
class Widgets(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Simple Web Browser")
        self.widget = QWidget(self)
        self.webview = QWebView()
        self.webview.load(QUrl("http://www.recursospython.com/"))
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.webview)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        QMetaObject.connectSlotsByName(self)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    sys.exit(app.exec_())