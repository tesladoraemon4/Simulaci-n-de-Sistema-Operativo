import sys
from nodoConectUI import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class nodoConect(QtGui.QDialog):
    def __init__(self,nodoO=None,nodos=[],parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        cont = 0
        self.POST = {}
        self.ui.selectNodoOrigen.addItem(""+str(nodoO.valStr)+"("+str(nodoO.id)+")")
        for n in nodos:
            if n != nodoO:
                self.ui.selectNodoOrigen.addItem(""+str(n.valStr)+"("+str(n.id)+")")
            #self.ui.selectNodoOrigen.setItemText(cont, _translate("Dialog", ""+str(n.valStr)+"("+str(n.id)+")", None))
            self.ui.selectNodoDestino.addItem(""+str(n.valStr)+"("+str(n.id)+")")
            #self.ui.selectNodoDestino.setItemText(cont, _translate("Dialog", ""+str(n.valStr)+"("+str(n.id)+")", None))
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.aceptado)



    def aceptado(self):
        self.POST['NO'] = str(self.ui.selectNodoOrigen.currentText())
        self.POST['ND'] = str(self.ui.selectNodoDestino.currentText())
        #super().accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = nodoConect()
    myapp.show()
    sys.exit(app.exec_())
