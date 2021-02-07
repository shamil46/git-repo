import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(70, 30, 1800, 1000)
        self.setWindowTitle('Рисование')
        self.do_paint = 0
        self.setMouseTracking(True)
        self.button = QPushButton('Кнопка', self)
        self.button.resize(100, 30)
        self.button.clicked.connect(self.push_button)

    def paintEvent(self, event):
        if self.do_paint == 1:
            print(1)
            qp = QPainter()
            qp.begin(self)
            self.draw_round(qp)
            qp.end()
            self.do_paint = 0

    def push_button(self):
        self.do_paint = 1
        self.repaint()

    def draw_round(self, qp):
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255),
                           random.randrange(0, 255)))
        n = random.randrange(2, 600)
        qp.drawEllipse(random.randrange(100, 1500) - n // 2, random.randrange(30, 800) - n // 2, n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
