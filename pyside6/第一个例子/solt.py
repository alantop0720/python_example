import sys
import os

from PySide6 import QtCore, QtWidgets, QtGui
import ui_login #导入ui_login.py
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        ui = ui_login.Ui_Form()#实例化UI对象
        ui.setupUi(self)#初始化

    @QtCore.Slot()#槽函数用它装饰
    def login(self): #在Qt Designer中为登录按钮命名的槽函数；
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Hello world")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        ret = msgBox.exec()

if __name__ == "__main__":
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "D:/alantop_dir/alantop_sde/anaconda3/Lib/site-packages/PySide6/plugins/platforms"
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())