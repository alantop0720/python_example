from PySide6 import QtCore, QtWidgets, QtGui
import os
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("点这里")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.showMessage)

    @QtCore.Slot()
    def showMessage(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Hello world")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        ret = msgBox.exec()

if __name__ == "__main__":
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "D:/alantop_dir/alantop_sde/anaconda3/Lib/site-packages/PySide6/plugins/platforms"
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()

    sys.exit(app.exec())