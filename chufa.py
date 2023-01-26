import sys
import random
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import *


class Calculator(QObject):
    signal_num = Signal(int, int)
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.tihao = 0
        self.ui = QUiLoader().load('UI/chufa.ui')
        self.num_reset()
        self.ui.lineEdit_13.setText(str(self.tihao))

        self.corr = 0

        self.ui.pushButton.clicked.connect(self.pushButton_clicked)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.ui.pushButton_3.clicked.connect(self.num_reset)
        self.ui.pushButton_4.clicked.connect(self.pushButton_4_clicked)

    def pushButton_clicked(self):
        value1 = int(self.ui.lineEdit.text())
        value2 = int(self.ui.lineEdit_3.text())
        shang = int(value1 / value2)
        yushu = value1 - value2 * shang

        zuoda1 = int(self.ui.lineEdit_5.text())
        zuoda2 = int(self.ui.lineEdit_11.text())
        if (zuoda1 == shang) and (zuoda2 == yushu):
            self.ui.lineEdit_7.setText("作答正确！")
            self.corr=self.corr+1
        else:
            self.ui.lineEdit_7.setText("作答错误！")

    def pushButton_2_clicked(self):
        zuoda = self.ui.lineEdit_5.text()
        if (zuoda == ""):
            self.ui.lineEdit_9.setText("想抄答案？！没门！")
        else:
            value1 = int(self.ui.lineEdit.text())
            value2 = int(self.ui.lineEdit_3.text())
            shang = int(value1 / value2)
            yushu = value1 - value2 * shang
            result = "商" + str(shang) + "余" + str(yushu)
            self.ui.lineEdit_9.setText(result)

    def num_reset(self):
        temp1 = random.randint(10, 99)
        temp2 = random.randint(2, 9)

        self.ui.lineEdit.setText(str(temp1))
        self.ui.lineEdit_3.setText(str(temp2))

        self.tihao = self.tihao + 1
        self.ui.lineEdit_13.setText(str(self.tihao))
        str_clear = ""
        self.ui.lineEdit_5.setText(str_clear)
        self.ui.lineEdit_7.setText(str_clear)
        self.ui.lineEdit_9.setText(str_clear)
        self.ui.lineEdit_11.setText(str_clear)

    def pushButton_4_clicked(self):
        self.final=Finalshow()
        self.final.ui.show()
        self.signal_num.connect(self.final.receive_num)
        self.signal_num.emit(self.tihao,self.corr)


class Finalshow():
    def __init__(self):
        self.ui = QUiLoader().load('UI/final.ui')
        pass

    def receive_num(self, num1, num2):
        self.ui.lineEdit_2.setText(str(num1))
        self.ui.lineEdit_4.setText(str(num2))

def main():
    app = QApplication([])
    calc = Calculator()
    calc.ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
