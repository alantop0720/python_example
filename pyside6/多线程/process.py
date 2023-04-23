from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PySide6.QtCore import QProcess
import sys
import os



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("python3", ['dummy_script.py'])




    def process_finished(self):
        self.message("Process finished.")
        self.p = None

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "D:/alantop_dir/alantop_sde/anaconda3/Lib/site-packages/PySide6/plugins/platforms"
app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec_()