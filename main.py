import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y, w, h = randint(0, 800), randint(0, 600), randint(60, 200), randint(60, 200)
        qp.drawEllipse(x, y, w, h)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())