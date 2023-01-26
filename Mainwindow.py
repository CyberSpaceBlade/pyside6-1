import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader

import erweishujiajian
import sanweishujiajian
import chufa


class Mainwindow(QWidget):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)
        self.ui = QUiLoader().load('UI/mainwindow.ui')

        self.ui.pushButton.clicked.connect(self.pushButton_clicked)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_clicked)

    def pushButton_clicked(self):
        self.erweishu = erweishujiajian.Calculator()
        self.erweishu.ui.show()

    def pushButton_2_clicked(self):
        self.sanweishu = sanweishujiajian.Calculator()
        self.sanweishu.ui.show()

    def pushButton_3_clicked(self):
        self.chufa = chufa.Calculator()
        self.chufa.ui.show()


def main():
    app = QApplication([])
    main_win = Mainwindow()
    main_win.ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
