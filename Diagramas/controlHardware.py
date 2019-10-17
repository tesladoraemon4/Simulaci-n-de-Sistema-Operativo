import sys
from controlHardwareUI import *

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


class ventanaPrincipal(QtGui.QFrame):
    def __init__(self, parent=None):
        QtGui.QFrame.__init__(self,parent)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ventanaPrincipal()
    myapp.show()
    sys.exit(app.exec_())