#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       simplewebx.py
#
#       Copyright 2013 Recursos Python - www.recursospython.com
#
#
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QMetaObject, QUrl
from PyQt4.QtGui import (QHBoxLayout, QLineEdit, QMainWindow,
                         QPushButton, QVBoxLayout, QWidget)
from PyQt4.QtWebKit import QWebView
class Navegador(QMainWindow):
    """Es un navegador web.
    """
    def __init__(self,title = "Simple Web Browser",urlInit = "file:///home/david/Documentos/CreadorDiagramas/miDiagrama.html"):
        QMainWindow.__init__(self)
        self.setWindowTitle(title)
        self.widget = QWidget(self)
        
        # Widget para el navegador
        self.webview = QWebView()
        self.webview.load(QUrl(urlInit))
        self.webview.urlChanged.connect(self.url_changed)
        
        # Ir hacia atrás
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.webview.back)
        
        # Ir hacia adelante
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.webview.forward)
        
        # Actualizar la página
        self.refresh_button = QPushButton("Actualizar")
        self.refresh_button.clicked.connect(self.webview.reload)
        
        # Barra de direcciones
        self.url_text = QLineEdit()
        
        # Cargar la página actual
        self.go_button = QPushButton("Ir")
        self.go_button.clicked.connect(self.url_set)
        
        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.back_button)
        self.toplayout.addWidget(self.forward_button)
        self.toplayout.addWidget(self.refresh_button)
        self.toplayout.addWidget(self.url_text)
        self.toplayout.addWidget(self.go_button)
        
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.toplayout)
        self.layout.addWidget(self.webview)
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        QMetaObject.connectSlotsByName(self)
    
    def url_changed(self, url):
        """Actualizar la barra de direcciones.
            Parámetros:
                (url:str)
                url => es la url para actualizar en el navegador.
            Retorno:
                void
        """
        self.url_text.setText(url.toString())
    
    def url_set(self):
        """Acceder a un nuevo URL.
            Parámetros:
                (void)
            Retorno:
                void
        """
        self.webview.setUrl(QUrl(self.url_text.text()))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    sys.exit(app.exec_())