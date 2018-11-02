import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


    def main_text_replace(self, string):
        self.ui.textEdit.setText(string)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
w.main_text_replace("Hello...")
sys.exit(app.exec_())